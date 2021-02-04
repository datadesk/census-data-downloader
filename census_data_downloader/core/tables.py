#! /usr/bin/env python
# -*- coding: utf-8 -*
"""
A base class that governs how to download and process tables from a Census API table.
"""
import os
import logging
import pathlib
from . import geotypes
from . import decorators
logger = logging.getLogger(__name__)


class BaseTableConfig(object):
    """
    Configures how to download and process tables from the Census API.
    """
    THIS_DIR = pathlib.Path(__file__).parent
    PARENT_DIR = THIS_DIR.parent
    # All available years
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
    # All available geographies
    GEOTYPE_LIST = (
        "nationwide",
        "regions",
        "divisions",
        "states",
        "congressional_districts",
        "state_legislative_upper_districts",
        "state_legislative_lower_districts",
        "counties",
        "places",
        "urban_areas",
        "msas",
        "csas",
        "pumas",
        "nectas",
        "cnectas",
        "aiannh_homelands",
        "tracts",
        "zctas",
        "unified_school_districts",
        "elementary_school_districts",
        "secondary_school_districts",
        "alaska_native",
        "county_subdivision"
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
            self.years_to_download = [max(self.YEAR_LIST), ]

        # Validate the years
        for year in self.years_to_download:
            if year not in self.YEAR_LIST:
                error_msg = ("Data only available for the years"
                             f"{self.YEAR_LIST[-1]}-{self.YEAR_LIST[0]}.")
                raise NotImplementedError(error_msg)

        # Set the data directories
        if data_dir:
            self.data_dir = pathlib.Path(str(data_dir))
        else:
            self.data_dir = self.PARENT_DIR.joinpath("data")
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

    #
    # Geotype downloaders
    #

    @decorators.downloader
    def download_nationwide(self):
        """
        Download nationwide data.
        """
        return geotypes.NationwideDownloader

    @decorators.downloader
    def download_regions(self):
        """
        Download data for all regions.
        """
        return geotypes.RegionsDownloader

    @decorators.downloader
    def download_divisions(self):
        """
        Download data for all divisions.
        """
        return geotypes.DivisionsDownloader

    @decorators.downloader
    def download_states(self):
        """
        Download data for all states.
        """
        return geotypes.StatesDownloader

    @decorators.downloader
    def download_congressional_districts(self):
        """
        Download data for all Congressional districts.
        """
        return geotypes.CongressionalDistrictsDownloader

    @decorators.downloader
    def download_state_legislative_upper_districts(self):
        """
        Download data for all Census upper legislative districts in the provided state.
        """
        return geotypes.StateLegislativeUpperDistrictsDownloader

    @decorators.downloader
    def download_state_legislative_lower_districts(self):
        """
        Download data for all Census lower legislative districts in the provided state.
        """
        return geotypes.StateLegislativeLowerDistrictsDownloader

    @decorators.downloader
    def download_counties(self):
        """
        Download data for all counties.
        """
        return geotypes.CountiesDownloader

    @decorators.downloader
    def download_places(self):
        """
        Download data for all Census designated places.
        """
        return geotypes.PlacesDownloader

    @decorators.downloader
    def download_urban_areas(self):
        """
        Download data for all urban areas
        """
        return geotypes.UrbanAreasDownloader

    @decorators.downloader
    def download_msas(self):
        """
        Download data for Metropolitian Statistical Areas.
        """
        return geotypes.MsasDownloader

    @decorators.downloader
    def download_csas(self):
        """
        Download data for Combined Statistical Areas.
        """
        return geotypes.CsasDownloader

    @decorators.downloader
    def download_pumas(self):
        """
        Download data for Public Use Microdata Areas.
        """
        return geotypes.PumasDownloader

    @decorators.downloader
    def download_nectas(self):
        """
        Download data for New England cities and towns.
        """
        return geotypes.NectasDownloader

    @decorators.downloader
    def download_cnectas(self):
        """
        Download data for combined New England cities and towns.
        """
        return geotypes.CnectasDownloader

    @decorators.downloader
    def download_aiannh_homelands(self):
        """
        Download data for American Indian home lands.
        """
        return geotypes.AiannhHomelandsDownloader

    @decorators.downloader
    def download_tracts(self):
        """
        Download data for all Census tracts in the provided state.
        """
        return geotypes.TractsDownloader

    @decorators.downloader
    def download_zctas(self):
        """
        Download data for Zip Code Tabulation Areas
        """
        return geotypes.ZctasDownloader

    @decorators.downloader
    def download_unified_school_districts(self):
        """
        Download data for unified school districts.
        """
        return geotypes.UnifiedSchoolDistrictsDownloader

    @decorators.downloader
    def download_elementary_school_districts(self):
        """
        Download data for elementary school districts.
        """
        return geotypes.ElementarySchoolDistrictsDownloader

    @decorators.downloader
    def download_secondary_school_districts(self):
        """
        Download data for secondary school districts.
        """
        return geotypes.SecondarySchoolDistrictsDownloader

    @decorators.downloader
    def download_alaska_native(self):
        """
        Download data for Alaska Native regional corporations.
        """
        return geotypes.AlaskaNativeDownloader

    @decorators.downloader
    def download_county_subdivision(self):
        """
        Download data for county subdivisions.
        """
        return geotypes.CountySubdivisionDownloader

    def download_everything(self):
        """
        Download 'em all.
        """
        for geo in self.GEOTYPE_LIST:
            print(geo)
            # Get the downloader function
            dl = getattr(self, f"download_{geo}", None)
            # Validate it
            if not dl or not callable(dl):
                raise NotImplementedError(f"Invalid geography type: {geo}")
            # Run it
            try:
                dl()
            except NotImplementedError:
                pass
