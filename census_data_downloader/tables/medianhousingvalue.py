#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class MedianHousingValueDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "medianhousingvalue"
    UNIVERSE = "owner-occupied housing units"
    RAW_TABLE_NAME = 'B25077'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001E": "median"
    })
