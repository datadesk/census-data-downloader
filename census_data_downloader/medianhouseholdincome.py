#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class MedianHouseholdIncomeDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincome"
    RAW_TABLE_NAME = 'B19013'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001E": "median"
    })


@register_downloader
class MedianHouseholdIncomeLatinoDownloader(MedianHouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincomelatino"
    RAW_TABLE_NAME = 'B19013I'


@register_downloader
class MedianHouseholdIncomeWhiteDownloader(MedianHouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincomewhite"
    RAW_TABLE_NAME = 'B19013H'


@register_downloader
class MedianHouseholdIncomeBlackDownloader(MedianHouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincomeblack"
    RAW_TABLE_NAME = 'B19013B'


@register_downloader
class MedianHouseholdIncomeAsianDownloader(MedianHouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "medianhouseholdincomeasian"
    RAW_TABLE_NAME = 'B19013D'
