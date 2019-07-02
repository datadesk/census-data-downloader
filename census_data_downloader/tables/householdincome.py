#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class HouseholdIncomeDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "householdincome"
    UNIVERSE = "households"
    RAW_TABLE_NAME = 'B19001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "10_and_under",
        '003': "10_15",
        '004': "15_20",
        '005': "20_25",
        '006': "25_30",
        '007': "30_35",
        '008': "35_40",
        '009': "40_45",
        '010': "45_50",
        '011': "50_60",
        '012': "60_75",
        '013': "75_100",
        '014': "100_125",
        '015': "125_150",
        '016': "150_200",
        '017': "200_and_up"
    })


@register
class HouseholdIncomeLatinoDownloader(HouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "householdincomelatino"
    RAW_TABLE_NAME = 'B19001I'


@register
class HouseholdIncomeWhiteDownloader(HouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "householdincomewhite"
    RAW_TABLE_NAME = 'B19001H'


@register
class HouseholdIncomeBlackDownloader(HouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "householdincomeblack"
    RAW_TABLE_NAME = 'B19001B'


@register
class HouseholdIncomeAsianDownloader(HouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "householdincomeasian"
    RAW_TABLE_NAME = 'B19001D'
