#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class HouseholdIncomeDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "householdincome"
    RAW_TABLE_NAME = 'B19001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': "universe",
        '002E': "10_and_under",
        '003E': "10_15",
        '004E': "15_20",
        '005E': "20_25",
        '006E': "25_30",
        '007E': "30_35",
        '008E': "35_40",
        '009E': "40_45",
        '010E': "45_50",
        '011E': "50_60",
        '012E': "60_75",
        '013E': "75_100",
        '014E': "100_125",
        '015E': "125_150",
        '016E': "150_200",
        '017E': "200_and_up"
    })


@register_downloader
class HouseholdIncomeLatinoDownloader(HouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "householdincomelatino"
    RAW_TABLE_NAME = 'B19001I'


@register_downloader
class HouseholdIncomeWhiteDownloader(HouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "householdincomewhite"
    RAW_TABLE_NAME = 'B19001H'


@register_downloader
class HouseholdIncomeBlackDownloader(HouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "householdincomeblack"
    RAW_TABLE_NAME = 'B19001B'


@register_downloader
class HouseholdIncomeAsianDownloader(HouseholdIncomeDownloader):
    PROCESSED_TABLE_NAME = "householdincomeasian"
    RAW_TABLE_NAME = 'B19001D'
