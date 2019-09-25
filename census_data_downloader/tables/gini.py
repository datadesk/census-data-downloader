#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class GiniIndexDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "gini"
    UNIVERSE = "households"
    RAW_TABLE_NAME = 'B19083'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "gini_index"
    })
