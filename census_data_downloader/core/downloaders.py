#! /usr/bin/env python
# -*- coding: utf-8 -*
import time
import logging
import pandas as pd
from us import states
from census import Census
logger = logging.getLogger(__name__)


class BaseRawDataDownloader(object):
    """
    Base class for downloading raw data from the Census API.
    """
    def __init__(self, config, year):
        self.config = config
        self.year = year
        self.api = getattr(Census(self.config.CENSUS_API_KEY, year=year), self.config.source)
        # Validate
        valid_geotype_slugs = [gt.replace("_", "") for gt in self.config.GEO_LIST]
        if self.slug not in valid_geotype_slugs:
            raise NotImplementedError(f"Data only available for {', '.join(self.config.GEO_LIST)}")
        # Prepare raw field list
        self.api_fields = self.get_api_fields()

    def get_api_fields(self):
        """
        Returns the fields to be fetched from the API.
        """
        field_names = [f"{self.config.RAW_TABLE_NAME}_{f}" for f in self.config.RAW_FIELD_CROSSWALK.keys()]
        return ['NAME'] + field_names

    def get_api_data(self):
        """
        Returns the data we want from the API.
        """
        logger.debug(f"Downloading {self.slug} {self.config.PROCESSED_TABLE_NAME} data from the raw {self.config.RAW_TABLE_NAME} table in the {self.year} {self.config.source} count")
        # Get the raw data
        return self.api.get(self.api_fields, self.api_filter)

    def clean_api_data(self, api_data):
        """
        Tidy up raw data into a DataFrame.
        """
        # Convert it to a dataframe
        df = pd.DataFrame.from_records(api_data)
        # Rename the ugly NAME field
        return df.rename(columns={"NAME": "name"})

    def write_api_data(self, api_data, csv_path):
        """
        Write raw data to the file system.
        """
        # Clean it up
        df = self.clean_api_data(api_data)
        # Write it to disk
        logger.debug(f"Writing raw ACS table to {csv_path}")
        df.to_csv(csv_path, index=False, encoding="utf-8")

    def download(self):
        # Set the CSV name
        csv_name = f"{self.config.source}_{self.year}_{self.config.PROCESSED_TABLE_NAME}_{self.slug}.csv"
        csv_path = self.config.raw_data_dir.joinpath(csv_name)

        # Skip hitting the API if we've already got the file, as long as we're not forcing it.
        if csv_path.exists() and not self.config.force:
            logger.debug(f"Raw CSV already exists at {csv_path}")
            return csv_path

        # Get the data
        api_data = self.get_api_data()

        # Write it out
        self.write_api_data(api_data, csv_path)

        # Pause to be polite to the API.
        time.sleep(1)

        # Hand the path back
        return csv_path


class BaseStateLevelRawDataDownloader(BaseRawDataDownloader):
    """
    Download and stitch together raw data the Census API only provides state by state.
    """
    def get_api_data(self):
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


class NationwideRawDownloader(BaseRawDataDownloader):
    """
    Download raw data at the nationwide level.
    """
    slug = "nationwide"
    api_filter = {'for': 'us:1'}
    geoid_function = lambda row: 1


class StatesRawDownloader(BaseRawDataDownloader):
    """
    Download raw data at the state level.
    """
    slug = "states"
    api_filter = {'for': 'state:*'}
    geoid_function = lambda row: row['state']


class CongressionalDistrictsRawDownloader(BaseRawDataDownloader):
    """
    Download raw data at the congressional-district level.
    """
    slug = "congressionaldistricts"
    api_filter = {'for': 'congressional district:*'}
    geoid_function = lambda row: row['state'] + row['congressional district']


class CountiesRawDownloader(BaseRawDataDownloader):
    """
    Download raw data at the county level.
    """
    slug = "counties"
    api_filter = {'for': 'county:*'}
    geoid_function = lambda row: row['state'] + row['county']


class PlacesRawDownloader(BaseRawDataDownloader):
    """
    Download raw data at the place level.
    """
    slug = "places"
    api_filter = {'for': 'place:*'}
    geoid_function = lambda row: row['state'] + row['place']


class UrbanAreasRawDownloader(BaseRawDataDownloader):
    """
    Download raw data at the urban-area level.
    """
    slug = "urbanareas"
    api_filter = {'for': 'urban area:*'}
    geoid_function = lambda row: row['urban area']


class MsasRawDownloader(BaseRawDataDownloader):
    """
    Download raw data at the metropolitan-statistical-area level.
    """
    slug = "msas"
    api_filter = {'for': 'metropolitan statistical area/micropolitan statistical area:*'}
    geoid_function = lambda row: row['metropolitan statistical area/micropolitan statistical area']


class CsasRawDownloader(BaseRawDataDownloader):
    """
    Download raw data at the combined-statistical-area level.
    """
    slug = "csas"
    api_filter = {'for': 'combined statistical area:*'}
    geoid_function = lambda row: row['combined statistical area']


class PumasRawDownloader(BaseRawDataDownloader):
    """
    Download raw data at the public-use-microdata level.
    """
    slug = "pumas"
    api_filter = {'for': 'public use microdata area:*'}
    geoid_function = lambda row: row['public use microdata area']


class AiannhHomelandsRawDownloader(BaseRawDataDownloader):
    """
    Download raw data at the Native American homeland level.
    """
    slug = "aiannhhomelands"
    api_filter = {'for': 'american indian area/alaska native area/hawaiian home land:*'}
    geoid_function = lambda row: row['american indian area/alaska native area/hawaiian home land']


class ZctasRawDownloader(BaseRawDataDownloader):
    """
    Download raw data at the zipcode-tabulation-area level.
    """
    slug = "zctas"
    api_filter = {'for': 'zip code tabulation area:*'}
    geoid_function = lambda row: row['zip code tabulation area']


class StateLegislativeDistrictsUpperRawDownloader(BaseStateLevelRawDataDownloader):
    """
    Download raw data at the upper-level state-legislative-district level.
    """
    slug = "statelegislativeupperdistricts"
    geoid_function = lambda row: row['state'] + row['state legislative district (upper chamber)']

    def get_api_filter(self, state):
        return {
            'for': 'state legislative district (upper chamber):*',
            'in': 'state: {}'.format(state.fips)
        }


class StateLegislativeLowerDistrictsRawDownloader(BaseStateLevelRawDataDownloader):
    """
    Download raw data at the lower-level state-legislative-district level.
    """
    slug = "statelegislativelowerdistricts"
    geoid_function = lambda row: row['state'] + row['lower legislative district (upper chamber)']

    def get_api_filter(self, state):
        return {
            'for': 'state legislative district (lower chamber):*',
            'in': 'state: {}'.format(state.fips)
        }


class TractsRawDownloader(BaseStateLevelRawDataDownloader):
    """
    Download raw data at the tract level.
    """
    slug = "tracts"
    geoid_function = lambda row: row['state'] + row['county'] + row['tract']

    def get_api_filter(self, state):
        return {
            'for': 'tract:*',
            'in': 'state: {}'.format(state.fips)
        }
