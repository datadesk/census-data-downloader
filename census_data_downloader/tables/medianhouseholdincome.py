#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class MedianHouseholdIncomeDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "medianhouseholdincome"
    UNIVERSE = "households"
    RAW_TABLE_NAME = 'B19013'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "median"
    })


@register
class MedianHouseholdIncomeLatinoDownloader(MedianHouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincomelatino"
    RAW_TABLE_NAME = 'B19013I'


@register
class MedianHouseholdIncomeWhiteDownloader(MedianHouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincomewhite"
    RAW_TABLE_NAME = 'B19013H'


@register
class MedianHouseholdIncomeBlackDownloader(MedianHouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincomeblack"
    RAW_TABLE_NAME = 'B19013B'


@register
class MedianHouseholdIncomeAsianDownloader(MedianHouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincomeasian"
    RAW_TABLE_NAME = 'B19013D'
