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
        '002': "0_9999",
        '003': "10000_15000",
        '004': "15000_20000",
        '005': "20000_25000",
        '006': "25000_30000",
        '007': "30000_35000",
        '008': "35000_40000",
        '009': "40000_45000",
        '010': "45000_50000",
        '011': "50000_60000",
        '012': "60000_75000",
        '013': "75000_100000",
        '014': "100000_125000",
        '015': "125000_150000",
        '016': "150000_200000",
        '017': "200000_more"
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
