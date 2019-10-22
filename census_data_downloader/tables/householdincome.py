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
        '003': "10000_14999",
        '004': "15000_19999",
        '005': "20000_24999",
        '006': "25000_29999",
        '007': "30000_34999",
        '008': "35000_39999",
        '009': "40000_44999",
        '010': "45000_49999",
        '011': "50000_59999",
        '012': "60000_74999",
        '013': "75000_99999",
        '014': "100000_124999",
        '015': "125000_149999",
        '016': "150000_199999",
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
