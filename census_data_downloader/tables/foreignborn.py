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
        "001": "universe",
        "002": "native",
        "013": "foreign_born"
    })


@register
class CitizenDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "citizenstatus"
    UNIVERSE = "total population"
    RAW_TABLE_NAME = "B05001"
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "universe",
        "002": "us_citizen_born_us",
        "003": "us_citizen_born_puertorico_or_us_island",
        "004": "us_citizen_born_abroad_american_parents",
        "005": "us_citizen_by_naturalization",
        "006": "not_us_citizen"
    })

    def process(self, *args, **kwargs):
        df = super().process(*args, **kwargs)
        # Our custom race groups
        df['us_citizen_total'] = df[[
            'us_citizen_born_us',
            'us_citizen_born_puertorico_or_us_island',
            'us_citizen_born_abroad_american_parents',
            'us_citizen_by_naturalization'
        ]].sum(axis=1)
        return df
