#! /usr/bin/env python
# -*- coding: utf-8 -*
"""
Handlers to process table configurations for each of the Census' different geography types.
"""
import time
import logging
import collections
import pandas as pd
from us import states
from census import Census
logger = logging.getLogger(__name__)

# Base downloader classes


class BaseGeoTypeDownloader(object):
    """
    Base class for downloading raw data from the Census API.

    Expects a TableConfig instance and year as input.
    """
    YEAR_LIST = [
        2019,
        2018,
        2017,
        2016,
        2015,
        2014,
        2013,
        2012,
        2011,
        2010,
        2009
    ]

    def __init__(self, config, year):
        # Set the input variables
        self.config = config
        self.year = year

        # Connect to the Census API for the provided source
        self.api = getattr(Census(self.config.CENSUS_API_KEY, year=year), self.config.source)

        # Validate the year
        if self.year not in self.YEAR_LIST:
            raise NotImplementedError("Census API does not support this year for this geotype")

        # Validate the geotype
        valid_geotype_slugs = [gt.replace("_", "") for gt in self.config.GEOTYPE_LIST]
        if self.slug not in valid_geotype_slugs:
            raise NotImplementedError(f"Data only available for {', '.join(self.config.GEOTYPE_LIST)}")

        # Prepare raw field list
        self.api_fields = self.get_api_fields()

        # Set the CSV names
        self.raw_csv_name = f"{self.config.source}_{self.year}_{self.config.PROCESSED_TABLE_NAME}_{self.slug}.csv"
        self.raw_csv_path = self.config.raw_data_dir.joinpath(self.raw_csv_name)
        self.processed_csv_name = f"{self.config.source}_{self.year}_{self.config.PROCESSED_TABLE_NAME}_{self.slug}.csv"
        self.processed_csv_path = self.config.processed_data_dir.joinpath(self.processed_csv_name)

    @property
    def api_filter(self):
        """
        Returns the filter that will retrieve the correct data from the API.
        """
        return {'for': f'{self.raw_geotype}:*'}

    def get_api_fields(self):
        """
        Returns the fields to be fetched from the API.
        """
        return list(self.get_raw_field_map().keys())

    def get_raw_field_map(self):
        """
        Returns a crosswalk between the raw API fields and our processed humanized field names.
        """
        """
        API doesn't have margin of error for 2009, so we will need a different crosswalk for the 2009 data.
        """
        if self.year == 2009:
            field_map_2009 = collections.OrderedDict({
                'NAME': "name"
            })
            field_suffix_map_2009 = {
                "E": "",
                "M": "_moe"
            }
            for field_id, field_name in self.config.RAW_FIELD_CROSSWALK.items():
                for field_suffix, name_suffix in field_suffix_map_2009.items():
                    full_raw_id = f"{self.config.RAW_TABLE_NAME}_{field_id}{field_suffix}"
                    processed_name = f"{field_name}{name_suffix}".strip()
                    field_map_2009[full_raw_id] = processed_name
            return field_map_2009
        else:
            field_map = collections.OrderedDict({
                'NAME': "name"
            })
            field_suffix_map = {
                "E": "",
                "EA": "_annotation",
                "M": "_moe",
                "MA": "_moe_annotation"
            }
            for field_id, field_name in self.config.RAW_FIELD_CROSSWALK.items():
                for field_suffix, name_suffix in field_suffix_map.items():
                    full_raw_id = f"{self.config.RAW_TABLE_NAME}_{field_id}{field_suffix}"
                    processed_name = f"{field_name}{name_suffix}".strip()
                    field_map[full_raw_id] = processed_name
        return field_map

    def get_raw_data(self):
        """
        Returns the data we want from the API.
        """
        logger.debug(f"Downloading {self.slug} {self.config.PROCESSED_TABLE_NAME} data from raw {self.config.RAW_TABLE_NAME} table in {self.year} {self.config.source} count")
        # Get the raw data
        return self.api.get(self.api_fields, self.api_filter)

    def create_geoid(self, row):
        """
        Create the unique identifier we prefer for this geotype.
        """
        return row[self.raw_geotype]

    def download(self):
        """
        Downloads raw data from the Census API.
        Returns path to CSV.
        """
        # Skip hitting the API if we've already got the file, as long as we're not forcing it.
        if self.raw_csv_path.exists() and not self.config.force:
            logger.debug(f"Raw CSV already exists at {self.raw_csv_path}")
            return self.raw_csv_path

        # Get the data
        data = self.get_raw_data()

        # Convert it to a dataframe
        df = pd.DataFrame.from_records(data)

        # Write it to disk
        logger.debug(f"Writing raw ACS table to {self.raw_csv_path}")
        df.to_csv(self.raw_csv_path, index=False, encoding="utf-8")

        # Pause to be polite to the API.
        time.sleep(0.5)

        # Hand the path back
        return self.raw_csv_path

    def process(self):
        """
        Converts the raw file to be used by humans.

        Returns path to CSV.
        """
        # Figure out where to write it
        if self.processed_csv_path.exists() and not self.config.force:
            logger.debug(f"Processed CSV already exists at {self.processed_csv_path}")
            return self.processed_csv_path

        # Read in the raw CSV of data from the ACS
        df = pd.read_csv(self.raw_csv_path, dtype=str)

        # Get the crosswalk between raw and processed field names
        field_name_mapper = self.get_raw_field_map()

        # Cast numbers to floats
        for field in field_name_mapper.keys():
            if "_" in field and (field.endswith("E") or field.endswith("M")):
                df[field] = df[field].astype(pd.np.float64)

        # Rename fields with humanized names
        df.rename(columns=field_name_mapper, inplace=True)

        # Add a combined GEOID column with a Census unique identifer
        df['geoid'] = df.apply(self.create_geoid, axis=1)

        if hasattr(self.config, 'process'):
            df = self.config.process(df)

        # Write it out
        logger.debug(f"Writing CSV to {self.processed_csv_path}")
        df.set_index(["geoid", "name"]).to_csv(
            self.processed_csv_path,
            index=True,
            encoding="utf-8"
        )
        return self.processed_csv_path


class BaseStateLevelGeoTypeDownloader(BaseGeoTypeDownloader):
    """
    Download and stitch together raw data the Census API only provides state by state.
    """
    def get_api_filter(self, state):
        """
        Returns an API filter to retrieve the correct data for the provided state.
        """
        return {
            'for': f'{self.raw_geotype}:*',
            'in': f'state: {state.fips}'
        }

    def get_raw_data(self):
        """
        Returns the data we want from the API.
        """
        api_data = []
        for state in states.STATES:
            logger.debug(f"Downloading {self.slug} {self.config.PROCESSED_TABLE_NAME} data from the raw {self.config.RAW_TABLE_NAME} table in {state} for the {self.year} {self.config.source} count")
            # Get the raw data
            api_filter = self.get_api_filter(state)
            state_data = self.api.get(self.api_fields, api_filter)
            api_data.extend(state_data)
        return api_data

    def create_geoid(self, row):
        return row['state'] + row[self.raw_geotype]

#
# Geotype downloaders
#


class NationwideDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the nationwide level.
    """
    slug = "nationwide"
    raw_geotype = "us"

    @property
    def api_filter(self):
        return {'for': 'us:1'}

    def create_geoid(self, row):
        return 1


class RegionsDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the region level.
    """
    slug = "regions"
    raw_geotype = "region"


class DivisionsDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the division level.
    """
    slug = "divisions"
    raw_geotype = "division"


class StatesDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the state level.
    """
    slug = "states"
    raw_geotype = "state"


class CongressionalDistrictsDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the congressional-district level.
    """
    slug = "congressionaldistricts"
    raw_geotype = "congressional district"

    def create_geoid(self, row):
        return row['state'] + row[self.raw_geotype]


class StateLegislativeUpperDistrictsDownloader(BaseStateLevelGeoTypeDownloader):
    """
    Download raw data at the upper-level state-legislative-district level.
    """
    slug = "statelegislativeupperdistricts"
    raw_geotype = "state legislative district (upper chamber)"


class StateLegislativeLowerDistrictsDownloader(BaseStateLevelGeoTypeDownloader):
    """
    Download raw data at the lower-level state-legislative-district level.
    """
    slug = "statelegislativelowerdistricts"
    raw_geotype = "state legislative district (lower chamber)"


class CountiesDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the county level.
    """
    slug = "counties"
    raw_geotype = "county"

    def create_geoid(self, row):
        return row['state'] + row[self.raw_geotype]


class PlacesDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the place level.
    """
    slug = "places"
    raw_geotype = "place"

    def create_geoid(self, row):
        return row['state'] + row[self.raw_geotype]


class UrbanAreasDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the urban-area level.
    """
    slug = "urbanareas"
    raw_geotype = "urban area"


class MsasDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the metropolitan-statistical-area level.
    """
    slug = "msas"
    raw_geotype = "metropolitan statistical area/micropolitan statistical area"


class CsasDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the combined-statistical-area level.
    """
    slug = "csas"
    raw_geotype = "combined statistical area"


class PumasDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the public-use-microdata level.
    """
    slug = "pumas"
    raw_geotype = "public use microdata area"


class NectasDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the New England city and town level.
    """
    slug = "nectas"
    raw_geotype = "new england city and town area"


class CnectasDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the combined New England city and town level.
    """
    YEAR_LIST = [
        2019,
        2018,
        2017,
        2016,
        2015,
        2014,
        2013,
        2012,
        2011,
        2010
    ]

    slug = "cnectas"
    raw_geotype = "combined new england city and town area"


class AiannhHomelandsDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the Native American homeland level.
    """
    slug = "aiannhhomelands"
    raw_geotype = "american indian area/alaska native area/hawaiian home land"


class TractsDownloader(BaseStateLevelGeoTypeDownloader):
    """
    Download raw data at the tract level.
    """
    slug = "tracts"
    raw_geotype = "tract"

    def create_geoid(self, row):
        return row['state'] + row['county'] + row[self.raw_geotype]


class ZctasDownloader(BaseGeoTypeDownloader):
    """
    Download raw data at the zipcode-tabulation-area level.
    """
    YEAR_LIST = [
        2019,
        2018,
        2017,
        2016,
        2015,
        2014,
        2013,
        2012,
        2011
    ]

    slug = "zctas"
    raw_geotype = "zip code tabulation area"


class UnifiedSchoolDistrictsDownloader(BaseStateLevelGeoTypeDownloader):
    """
    Download raw data at the unified school district level.
    """
    slug = "unifiedschooldistricts"
    raw_geotype = "school district (unified)"


class ElementarySchoolDistrictsDownloader(BaseStateLevelGeoTypeDownloader):
    """
    Download raw data at the elementary school district level.
    """
    slug = "elementaryschooldistricts"
    raw_geotype = "school district (elementary)"


class SecondarySchoolDistrictsDownloader(BaseStateLevelGeoTypeDownloader):
    """
    Download raw data at the secondary school district level.
    """
    slug = "secondaryschooldistricts"
    raw_geotype = "school district (secondary)"


class AlaskaNativeDownloader(BaseStateLevelGeoTypeDownloader):
    """
    Download raw data at the Alaska Native regional corporation level.
    """
    slug = "alaskanative"
    raw_geotype = "alaska native regional corporation"


class CountySubdivisionDownloader(BaseStateLevelGeoTypeDownloader):
    """
    Download raw data at the county subdivision level.
    """
    slug = "countysubdivision"
    raw_geotype = "county subdivision"
