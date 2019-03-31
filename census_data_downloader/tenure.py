#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader


class TenureDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "tenure"
    RAW_TABLE_NAME = 'B25003'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'housing_units',
        '002E': 'owner_occupied',
        '003E': 'renter_occupied'
    })


class TenureLatinoDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenurelatino"
    RAW_TABLE_NAME = 'B25003I'


class TenureWhiteDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenurewhite"
    RAW_TABLE_NAME = 'B25003H'


class TenureBlackDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenureblack"
    RAW_TABLE_NAME = 'B25003B'


class TenureAsianDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenureasian"
    RAW_TABLE_NAME = 'B25003D'
