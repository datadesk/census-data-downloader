#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
import census_data_aggregator
from census_data_downloader.core import MOE_MAP
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

    def process(self, df):
        def calculate_moe(row):
            # our custom groups
            if row['us_citizen_by_naturalization_moe'] in list(MOE_MAP.values()):
                value = sum([row['us_citizen_by_naturalization'], row['us_citizen_born_abroad_american_parents'], row['us_citizen_born_puertorico_or_us_island_alone'], row['us_citizen_born_us']])
                moe = None
            value, moe = census_data_aggregator.approximate_sum(
                (row['us_citizen_by_naturalization'], row['us_citizen_by_naturalization_moe']),
                (row['us_citizen_born_abroad_american_parents'], row['us_citizen_born_abroad_american_parents_moe']),
                (row['us_citizen_born_puertorico_or_us_island_alone'], row['us_citizen_born_puertorico_or_us_island_moe']),
                (row['us_citizen_born_us'], row['us_citizen_born_us_moe']),
            )
            row['us_citizen_total'] = value
            row['us_citizen_total_moe'] = moe
            return row

        df = df.apply(
            calculate_moe,
            axis=1
        )

        # Pass it back
        return df
