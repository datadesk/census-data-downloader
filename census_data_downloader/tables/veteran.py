#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class VeteranDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "veterans"
    UNIVERSE = "civilian veterans 18 years and over"
    RAW_TABLE_NAME = 'B21002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "universe"
    })
