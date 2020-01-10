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
        "001": "total",
        "002": "0_10000",
        "003": "10000_14999",
        "004": "15000_19999",
        "005": "20000_24999",
        "006": "25000_29999",
        "007": "30000_34999",
        "008": "35000_39999",
        "009": "40000_49999",
        "010": "50000_59999",
        "011": "60000_69999",
        "012": "70000_79999",
        "013": "80000_89999",
        "014": "90000_99999",
        "015": "100000_124999",
        "016": "125000_149999",
        "017": "150000_174999",
        "018": "175000_199999",
        "019": "200000_249999",
        "020": "250000_299999",
        "021": "300000_399999",
        "022": "400000_499999",
        "023": "500000_749999",
        "024": "750000_999999",
        "025": "1000000_1499999",
        "026": "1500000_1999999",
        "027": "2000000_more",
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
class TenurePopDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "tenurepop"
    UNIVERSE = "total population in occupied housing units"
    RAW_TABLE_NAME = 'B25008'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': 'universe',
        '002': 'owner_occupied',
        '003': 'renter_occupied'
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


@register
class MedianRentBedroomDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "mediangrossrentbybedroom"
    UNIVERSE = " renter-occupied housing units paying cash rent"
    RAW_TABLE_NAME = 'B25031'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': 'median_gross_rent',
        '003': 'median_gross_rent_1_bedroom'
    })


@register
class GrossRentBedroomDownloader(TenureDownloader):
    PROCESSED_TABLE_NAME = "grossrentbybedroom"
    UNIVERSE = "renter occupied housing units"
    RAW_TABLE_NAME = 'B25068'
    """ these are all one bed with cash rent, for the aggregator"""
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '011': 'total_one_bed',
        '012': 'total_one_bed_with_cash_rent',
        '013': '0_299',
        '014': '300_499',
        '015': '500_749',
        '016': '750_999',
        '017': '1000_1499',
        '018': '1500_more',
    })
