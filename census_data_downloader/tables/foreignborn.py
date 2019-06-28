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


@register
class CitizenDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "citizenstatus"
    UNIVERSE = "total population"
    RAW_TABLE_NAME = "B05001"
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001E": "universe",
        "002E": "us_citizen_born_us",
        "003E": "us_citizen_born_puertorico_or_us_island",
        "004E": "us_citizen_born_abroad_american_parents",
        "005E": "us_citizen_by_naturalization",
        "006E": "not_us_citizen"
    })
