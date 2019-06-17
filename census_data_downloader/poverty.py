#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class PovertyDownloader(BaseDownloader):
    YEAR_LIST = (2017,)
    PROCESSED_TABLE_NAME = "poverty_by_sex_and_age"
    UNIVERSE = "households"
    RAW_TABLE_NAME = 'B17001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'universe',
        '001M': 'universe_moe',
        '002E': 'universe_income_past12months_below_poverty_level',
        '002M': 'universe_income_past12months_below_poverty_level_moe',
        '003E': 'universe_income_past12months_below_poverty_level_male',
        '003M': 'universe_income_past12months_below_poverty_level_male_moe',
        '017E': 'universe_income_past12months_below_poverty_level_female',
        '017M': 'universe_income_past12months_below_poverty_level_female_moe',
        '031E': 'universe_income_past12months_at_or_below_poverty_level',
        '031M': 'universe_income_past12months_at_or_below_poverty_level_moe'
    })

