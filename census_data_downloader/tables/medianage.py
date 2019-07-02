#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class MedianAgeDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = 'medianage'
    UNIVERSE = "total population"
    RAW_TABLE_NAME = 'B01002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "median",
        "002": "male",
        "003": "female"
    })
