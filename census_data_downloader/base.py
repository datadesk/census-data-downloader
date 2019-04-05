#! /usr/bin/env python
# -*- coding: utf-8 -*
import os
import time
import logging
import pathlib
import pandas as pd
from us import states
from census import Census
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
            self.years_to_download = map(int, years)
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
        csv_suffix = "nationwide"
        api_filter = {'for': 'us:1'}
        geoid_function = lambda row: 1
        self._download_tables(api_filter, csv_suffix, geoid_function)

    def download_states(self):
        """
        Download data for all states.
        """
        csv_suffix = "states"
        api_filter = {'for': 'state:*'}
        geoid_function = lambda row: row['state']
        self._download_tables(api_filter, csv_suffix, geoid_function)

    def download_congressional_districts(self):
        """
        Download data for all Congressional districts.
        """
        csv_suffix = "congressionaldistricts"
        api_filter = {'for': 'congressional district:*'}
        geoid_function = lambda row: row['state'] + row['congressional district']
        self._download_tables(api_filter, csv_suffix, geoid_function)

    def download_counties(self):
        """
        Download data for all counties.
        """
        csv_suffix = "counties"
        api_filter = {'for': 'county:*'}
        geoid_function = lambda row: row['state'] + row['county']
        self._download_tables(api_filter, csv_suffix, geoid_function)

    def download_places(self):
        """
        Download data for all Census designated places.
        """
        csv_suffix = "places"
        api_filter = {'for': 'place:*'}
        geoid_function = lambda row: row['state'] + row['place']
        self._download_tables(api_filter, csv_suffix, geoid_function)

    def download_tracts(self, state):
        """
        Download data for all Census tracts in the provided state.
        """
        state_obj = getattr(states, state.upper())
        csv_suffix = f"tracts_{state_obj.abbr.lower()}"
        api_filter = {
            'for': 'tract:*',
            'in': f'state: {state_obj.fips}'
        }
        geoid_function = lambda row: row['state'] + row['county'] + row['tract']
        self._download_tables(api_filter, csv_suffix, geoid_function)

    def download_state_legislative_districts_upper(self, state):
        """
        Download data for all Census upper legislative districts in the provided state.
        """
        state_obj = getattr(states, state.upper())
        csv_suffix = f'statelegislativedistrictsupper_{state_obj.abbr.lower()}'
        api_filter = {
            'for': 'state legislative district (upper chamber):*',
            'in': f'state: {state_obj.fips}'
        }
        geoid_function = lambda row: row['state'] + row['state legislative district (upper chamber)']
        self._download_tables(api_filter, csv_suffix, geoid_function)

    def download_state_legislative_districts_lower(self, state):
        """
        Download data for all Census lower legislative districts in the provided state.
        """
        state_obj = getattr(states, state.upper())
        csv_suffix = f'statelegislativedistrictslower_{state_obj.abbr.lower()}'
        api_filter = {
            'for': 'state legislative district (lower chamber):*',
            'in': f'state: {state_obj.fips}'
        }
        geoid_function = lambda row: row['state'] + row['state legislative district (lower chamber)']
        self._download_tables(api_filter, csv_suffix, geoid_function)

    def download_usa(self):
        """
        Download all datasets that provide full coverage for the entire country.
        """
        self.download_nationwide()
        self.download_states()
        self.download_congressional_districts()
        self.download_counties()
        self.download_places()

    def download_everything(self):
        """
        Download 'em all.
        """
        self.download_usa()
        for state in states.STATES:
            self.download_tracts(state.abbr)
            self.download_state_legislative_districts_upper(state.abbr)
            self.download_state_legislative_districts_lower(state.abbr)

    def _download_tables(self, api_filter, csv_suffix, geoid_function):
        """
        Download and process data.
        """
        for year in self.years_to_download:
            # Set the year as a sneaky private variable we can access elsewhere
            self._year = year

            # Get the raw table
            raw_table = self._get_raw_table(year, api_filter, csv_suffix)

            # Figure out where to write it
            csv_name = f"{self.source}_{year}_{self.PROCESSED_TABLE_NAME}_{csv_suffix}.csv"
            csv_path = self.processed_data_dir.joinpath(csv_name)
            if csv_path.exists() and not self.force:
                logger.debug(f"Processed CSV already exists at {csv_path}")
                continue

            # Process it
            processed_table = self._process_raw_data(raw_table)

            # Add a combined GEOID column with a Census unique identifer
            processed_table['geoid'] = processed_table.apply(geoid_function, axis=1)

            # Write it out
            logger.debug(f"Writing CSV to {csv_path}")
            processed_table.set_index(["geoid", "name"]).to_csv(
                csv_path,
                index=True,
                encoding="utf-8"
            )

    def _get_raw_table(self, year, api_filter, csv_suffix):
        """
        Retrieve the Census API data and return it as an dataframe.
        """
        # Set the CSV name
        csv_name = f"{self.source}_{year}_{self.PROCESSED_TABLE_NAME}_{csv_suffix}.csv"
        csv_path = self.raw_data_dir.joinpath(csv_name)

        # Skip hitting the API if we've already got the file, as long as we're not forcing it.
        if csv_path.exists() and not self.force:
            logger.debug(f"Raw CSV already exists at {csv_path}")
            return csv_path

        # Set the fields we want to pull from API
        field_names = [f"{self.RAW_TABLE_NAME}_{f}" for f in self.RAW_FIELD_CROSSWALK.keys()]
        field_list = ['NAME'] + field_names

        # Hit the API
        logger.debug(f"Downloading raw {self.source} {self.RAW_TABLE_NAME} table for {year} filtered to {api_filter}")
        self.api = getattr(Census(self.CENSUS_API_KEY, year=year), self.source)
        data = self.api.get(field_list, api_filter)

        # Convert it to a DataFrame
        df = pd.DataFrame.from_records(data)

        # Rename the ugly NAME field
        df.rename(columns={"NAME": "name"}, inplace=True)

        # Write it to disk
        logger.debug(f"Writing raw ACS table to {csv_path}")
        df.to_csv(csv_path, index=False, encoding="utf-8")

        # Pause to be polite to the API.
        time.sleep(1)

        # Return the path
        return csv_path

    def _process_raw_data(self, path):
        """
        Accepts a path to a CSV with raw ACS data from the Census API.

        Returns it polished for human analysis.
        """
        # Read in the raw CSV of data from the ACS
        df = pd.read_csv(
            path,
            dtype={
                "state": str,
                "county": str,
                "place": str,
                "tract": str,
                "congressional district": str,
                "state legislative district (upper chamber)": str,
                "state legislative district (lower chamber)": str
            }
        )

        # Rename fields with humanized names
        field_name_mapper = dict(
            (f"{self.RAW_TABLE_NAME}_{raw}", processed)
            for raw, processed in self.RAW_FIELD_CROSSWALK.items()
        )
        df.rename(columns=field_name_mapper, inplace=True)

        # Cast numbers to integers
        for field in field_name_mapper.values():
            df[field].astype(pd.np.float64)

        # Pass it back
        return df
