#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class MobilityDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "mobility"
    UNIVERSE = "population 1 year and over"
    RAW_TABLE_NAME = 'B07003'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '004': "same_house",
        '007': "moved_within_county",
        '010': "moved_from_different_county_in_same_state",
        '013': "moved_from_different_state",
        '016': "moved_from_abroad",
    })


@register
class MobilityBySexDownloader(MobilityDownloader):
    PROCESSED_TABLE_NAME = "mobilitybysex"
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "male_total",
        '003': "female_total",
        '004': "total_same_house",
        '005': "male_same_house",
        '006': "female_same_house",
        '007': "total_moved_within_county",
        '008': "male_moved_within_county",
        '009': "female_moved_within_county",
        '010': "total_moved_from_different_county_in_same_state",
        '011': "male_moved_from_different_county_in_same_state",
        '012': "female_moved_from_different_county_in_same_state",
        '013': "total_moved_from_different_state",
        '014': "male_moved_from_different_state",
        '015': "female_moved_from_different_state",
        '016': "total_moved_from_abroad",
        '017': "male_moved_from_abroad",
        '018': "female_moved_from_abroad"
    })


@register
class MobilityWhiteDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "mobilitywhite"
    UNIVERSE = "population 1 year and over"
    RAW_TABLE_NAME = 'B07004H'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "same_house",
        '003': "moved_within_county",
        '004': "moved_from_different_county_in_same_state",
        '005': "moved_from_different_state",
        '006': "moved_from_abroad"
    })


@register
class MobilityBlackDownloader(MobilityWhiteDownloader):
    PROCESSED_TABLE_NAME = "mobilityblack"
    RAW_TABLE_NAME = 'B07004B'


@register
class MobilityAsianDownloader(MobilityWhiteDownloader):
    PROCESSED_TABLE_NAME = "mobilityasian"
    RAW_TABLE_NAME = 'B07004D'


@register
class MobilityLatinoDownloader(MobilityWhiteDownloader):
    PROCESSED_TABLE_NAME = "mobilitylatino"
    RAW_TABLE_NAME = 'B07004I'


@register
class MobilityByCitizenship(BaseTableConfig):
    PROCESSED_TABLE_NAME = "mobilitybycitizenship"
    UNIVERSE = "population 1 year and over"
    RAW_TABLE_NAME = 'B07007'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "native",
        '003': "foreign_born",
        '004': "foreign_born_naturalized_us_citizen",
        '005': "foreign_born_not_us_citizen",
        '006': "same_house_1_year_ago",
        '007': "same_house_1_year_ago_native",
        '008': "same_house_1_year_ago_foreign_born",
        '009': "same_house_1_year_ago_foreign_born_naturalized_us_citizen",
        '010': "same_house_1_year_ago_foreign_born_not_us_citizen",
        '011': "moved_within_same_county",
        '012': "moved_within_same_county_native",
        '013': "moved_within_same_county_foreign_born",
        '014': "moved_within_same_county_foreign_born_naturalized_us_citizen",
        '015': "moved_within_same_county_foreign_born_not_us_citizen",
        '016': "moved_from_different_county_within_same_state",
        '017': "moved_from_different_county_within_same_state_native",
        '018': "moved_from_different_county_within_same_state_foreign_born",
        '019': "moved_from_different_county_within_same_state_foreign_born_naturalized_us_citizen",
        '020': "moved_from_different_county_within_same_state_foreign_born_not_us_citizen",
        '021': "moved_from_different_state",
        '022': "moved_from_different_state_native",
        '023': "moved_from_different_state_foreign_born",
        '024': "moved_from_different_state_foreign_born_naturalized_us_citizen",
        '025': "moved_from_different_state_foreign_born_not_us_citizen",
        '026': "moved_from_abroad",
        '027': "moved_from_abroad_native",
        '028': "moved_from_abroad_foreign_born",
        '029': "moved_from_abroad_foreign_born_naturalized_us_citizen",
        '030': "moved_from_abroad_foreign_born_not_us_citizen"
    })
