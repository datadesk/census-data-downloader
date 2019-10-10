#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class HousingValueDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "housingvalue"
    UNIVERSE = "owner occupied housing units"
    RAW_TABLE_NAME = "B25075"
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "01": "total",
        "02": "0_10000",
        "03": "10000_14999",
        "04": "15000_19999",
        "05": "20000_24999",
        "06": "25000_29999",
        "07": "30000_34999",
        "08": "35000_39999",
        "09": "40000_49999",
        "10": "50000_59999",
        "11": "60000_69999",
        "12": "70000_79999",
        "13": "80000_89999",
        "14": "90000_99999",
        "15": "100000_124999",
        "16": "125000_149999",
        "17": "150000_174999",
        "18": "175000_199999",
        "19": "200000_249999",
        "20": "250000_299999",
        "21": "300000_399999",
        "22": "400000_499999",
        "23": "500000_749999",
        "24": "750000_999999",
        "25": "1000000_1499999",
        "26": "1500000_1999999",
        "27": "2000000_more",
    })


@register
class MedianMonthlyHousingCostsDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "medianmonthlyhousingcosts"
    UNIVERSE = "occupied housing units with monthly housing costs"
    RAW_TABLE_NAME = "B25105"
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "median"
    })


@register
class MedianHousingValueDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "medianhousingvalue"
    UNIVERSE = "owner-occupied housing units"
    RAW_TABLE_NAME = 'B25077'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "median"
    })


@register
class MedianGrossRentDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "mediangrossrent"
    UNIVERSE = "renter-occupied housing units paying cash rent"
    RAW_TABLE_NAME = 'B25064'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "median"
    })


@register
class TenureDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "tenure"
    UNIVERSE = "occupied housing units"
    RAW_TABLE_NAME = 'B25003'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': 'universe',
        '002': 'owner_occupied',
        '003': 'renter_occupied'
    })


@register
class TenureLatinoDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenurelatino"
    RAW_TABLE_NAME = 'B25003I'


@register
class TenureWhiteDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenurewhite"
    RAW_TABLE_NAME = 'B25003H'


@register
class TenureBlackDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenureblack"
    RAW_TABLE_NAME = 'B25003B'


@register
class TenureAsianDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "tenureasian"
    RAW_TABLE_NAME = 'B25003D'
