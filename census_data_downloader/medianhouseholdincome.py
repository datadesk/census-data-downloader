#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader


class MedianHouseholdIncomeDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincome"
    RAW_TABLE_NAME = 'B19013'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001E": "median"
    })


class MedianHouseholdIncomeLatinoDownloader(MedianHouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincomelatino"
    RAW_TABLE_NAME = 'B19013I'


class MedianHouseholdIncomeWhiteDownloader(MedianHouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincomewhite"
    RAW_TABLE_NAME = 'B19013H'


class MedianHouseholdIncomeBlackDownloader(MedianHouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincomeblack"
    RAW_TABLE_NAME = 'B19013B'


class MedianHouseholdIncomeAsianDownloader(MedianHouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincomeasian"
    RAW_TABLE_NAME = 'B19013D'
