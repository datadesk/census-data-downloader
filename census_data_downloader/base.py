#! /usr/bin/env python
# -*- coding: utf-8 -*
import os
import time
import logging
import pathlib
import pandas as pd
from us import states
from census import Census
from .core import downloaders
logger = logging.getLogger(__name__)


class BaseDownloader(object):
    """
    Downloads and processes ACS tables from the Census API.
    """
    THIS_DIR = pathlib.Path(__file__).parent
    YEAR_LIST = (
        2017,
        2016,
        2015,
        2014,
        2013,
        2012,
        2011,
        2010,
        2009
    )

    # All available geographies
    # (Subclasses can override this)
    GEO_LIST = (
        "nationwide",
        "states",
        "congressional_districts",
        "counties",
        "places",
        "urban_areas",
        "msas",
        "csas",
        "pumas",
        "aiannh_homelands",
        "zctas",
        "state_legislative_upper_districts",
        "state_legislative_lower_districts",
        "tracts"
    )

    # Geographies only available on a per-state level
    # (Subclasses should not override this)
    STATE_ONLY_GEOS = (
        "tracts",
        "state_legislative_districts_upper",
        "state_legislative_districts_lower"
    )

    def __init__(
        self,
        api_key=None,
        source="acs5",
        years=None,
        data_dir=None,
        force=False
    ):
        """
        Configuration.
        """
        # Set the inputs
        self.CENSUS_API_KEY = os.getenv("CENSUS_API_KEY", api_key)
        if not self.CENSUS_API_KEY:
            raise NotImplementedError("Census API key required. Pass it as the first argument.")
        self.source = source
        self.force = force

        #
        # Allow custom years for data download, defaulting to most recent year
        #

        # If they want all the years, give it to them.
        if years == "all":
            self.years_to_download = self.YEAR_LIST
        # If the user provides a year give them that.
        elif isinstance(years, int):
            self.years_to_download = [years]
        # Or if they provide years as a list, give those then.
        elif isinstance(years, list):
            self.years_to_download = list(map(int, years))
        # If they provided nothing, default to the latest year of data
        elif years is None:
            self.years_to_download = (max(self.YEAR_LIST),)

        # Validate the years
        for year in self.years_to_download:
            if year not in self.YEAR_LIST:
                error_msg = ("Data only available for the years "
                             f"{self.YEAR_LIST[-1]}-{self.YEAR_LIST[0]}.")
                raise NotImplementedError(error_msg)

        # Set the data directories
        if data_dir:
            self.data_dir = pathlib.Path(str(data_dir))
        else:
            self.data_dir = self.THIS_DIR.joinpath("data")
        self.raw_data_dir = self.data_dir.joinpath("raw")
        self.processed_data_dir = self.data_dir.joinpath("processed")

        # Make sure they exist
        if not self.data_dir.exists():
            self.data_dir.mkdir()
        if not self.raw_data_dir.exists():
            self.raw_data_dir.mkdir()
        if not self.processed_data_dir.exists():
            self.processed_data_dir.mkdir()

    @property
    def censusreporter_url(self):
        """
        Returns the URL of the Census Reporter page explaining the ACS table.
        """
        return f"https://censusreporter.org/tables/{self.RAW_TABLE_NAME}/"

    def download_nationwide(self):
        """
        Download nationwide data.
        """
        for year in self.years_to_download:
            dl = downloaders.NationwideRawDownloader(self, year)
            dl.download()

    def download_states(self):
        """
        Download data for all states.
        """
        for year in self.years_to_download:
            dl = downloaders.StatesRawDownloader(self, year)
            dl.download()

    def download_congressional_districts(self):
        """
        Download data for all Congressional districts.
        """
        for year in self.years_to_download:
            dl = downloaders.CongressionalDistrictsRawDownloader(self, year)
            dl.download()

    def download_counties(self):
        """
        Download data for all counties.
        """
        for year in self.years_to_download:
            dl = downloaders.CountiesRawDownloader(self, year)
            dl.download()

    def download_places(self):
        """
        Download data for all Census designated places.
        """
        for year in self.years_to_download:
            dl = downloaders.PlacesRawDownloader(self, year)
            dl.download()

    def download_tracts(self):
        """
        Download data for all Census tracts in the provided state.
        """
        for year in self.years_to_download:
            dl = downloaders.TractsRawDownloader(self, year)
            dl.download()

    def download_state_legislative_upper_districts(self):
        """
        Download data for all Census upper legislative districts in the provided state.
        """
        for year in self.years_to_download:
            dl = downloaders.StateLegislativeUpperDistrictsRawDownloader(self, year)
            dl.download()

    def download_state_legislative_lower_districts(self):
        """
        Download data for all Census lower legislative districts in the provided state.
        """
        for year in self.years_to_download:
            dl = downloaders.StateLegislativeLowerDistrictsRawDownloader(self, year)
            dl.download()

    def download_urban_areas(self):
        """
        Download data for all urban areas
        """
        for year in self.years_to_download:
            dl = downloaders.UrbanAreasRawDownloader(self, year)
            dl.download()

    def download_msas(self):
        """
        Download data for Metropolitian Statistical Areas.
        """
        for year in self.years_to_download:
            dl = downloaders.MsasRawDownloader(self, year)
            dl.download()

    def download_csas(self):
        """
        Download data for Combined Statistical Areas.
        """
        for year in self.years_to_download:
            dl = downloaders.CsasRawDownloader(self, year)
            dl.download()

    def download_pumas(self):
        """
        Download data for Public Use Microdata Areas.
        """
        for year in self.years_to_download:
            dl = downloaders.PumasRawDownloader(self, year)
            dl.download()

    def download_aiannh_homelands(self):
        """
        Download data for American Indian home lands.
        """
        for year in self.years_to_download:
            dl = downloaders.AiannhHomelandsRawDownloader(self, year)
            dl.download()

    def download_zctas(self):
        """
        Download data for Zip Code Tabulation Areas
        """
        for year in self.years_to_download:
            dl = downloaders.ZctasRawDownloader(self, year)
            dl.download()

    def download_usa(self):
        """
        Download all datasets that provide full coverage for the entire country.
        """
        # Call the downloader for every available geography
        for geo in set(self.GEO_LIST) - set(self.STATE_ONLY_GEOS):
            download = getattr(self, f"download_{geo}", None)
            if not download or not callable(download):
                raise NotImplementedError(f"Invalid geography type: {geo}")
            else:
                download()

    def download_everything(self):
        """
        Download 'em all.
        """
        self.download_usa()
        for geo in set(self.GEO_LIST) & set(self.STATE_ONLY_GEOS):
            download = getattr(self, f"download_{geo}", None)
            if not download or not callable(download):
                raise NotImplementedError(f"Invalid geography type: {geo}")
            else:
                for state in states.STATES:
                    download(state.abbr)

    # def _download_tables(self, api_filter, csv_suffix, geoid_function):
    #     """
    #     Download and process data.
    #     """
    #     self.get_raw_tables()
    #     :
    #         # Set the year as a sneaky private variable we can access elsewhere
    #         self._year = year
    #
    #         # Get the raw table
    #         raw_table = self._get_raw_table(year, api_filter, csv_suffix)
    #
    #         # Process it
    #         processed_table = self._process_raw_data(raw_table)
    #
    #         # Add a combined GEOID column with a Census unique identifer
    #         processed_table['geoid'] = processed_table.apply(geoid_function, axis=1)
    #
    #         # Write it out
    #         logger.debug(f"Writing CSV to {csv_path}")
    #         processed_table.set_index(["geoid", "name"]).to_csv(
    #             csv_path,
    #             index=True,
    #             encoding="utf-8"
    #         )

    def _process_raw_data(self, raw_path, year, api_filter, csv_suffix):
        """
        Accepts a path to a CSV with raw ACS data from the Census API.

        Returns it polished for human analysis.
        """
        # Figure out where to write it
        csv_name = f"{self.source}_{year}_{self.PROCESSED_TABLE_NAME}_{csv_suffix}.csv"
        csv_path = self.processed_data_dir.joinpath(csv_name)
        if csv_path.exists() and not self.force:
            logger.debug(f"Processed CSV already exists at {csv_path}")
            return

        # Read in the raw CSV of data from the ACS
        df = pd.read_csv(raw_path, dtype=str)

        # Rename fields with humanized names
        field_name_mapper = dict(
            (f"{self.RAW_TABLE_NAME}_{raw}", processed)
            for raw, processed in self.RAW_FIELD_CROSSWALK.items()
        )
        df.rename(columns=field_name_mapper, inplace=True)

        # Cast numbers to floats
        for field in field_name_mapper.values():
            df[field].astype(pd.np.float64)

        # Pass it back
        return df
