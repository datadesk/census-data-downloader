#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class ForeignBornDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "foreignborn"
    UNIVERSE = "total population"
    RAW_TABLE_NAME = 'B05002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001E": "universe",
        "002E": "native",
        "013E": "foreign_born"
    })
