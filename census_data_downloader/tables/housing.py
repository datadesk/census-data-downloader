#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


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
