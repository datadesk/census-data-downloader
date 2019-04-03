#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader


class PovertyDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "poverty"
    RAW_TABLE_NAME = 'B17001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'total',
        '002E': 'below_poverty_level',
        '031E': 'above_poverty_level',
        '003E': 'male_below_poverty_level',
        '017E': 'female_below_poverty_level',
        '032E': 'male_above_poverty_level',
        '046E': 'female_above_poverty_level'
    })
