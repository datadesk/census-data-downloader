#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class PopulationDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "population"
    UNIVERSE = "total population"
    RAW_TABLE_NAME = "B01003"
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "universe"
    })
