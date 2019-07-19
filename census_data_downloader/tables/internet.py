#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from pprint import pprint
import census_data_aggregator
from census_data_downloader.core import MOE_MAP
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class InternetDownloader(BaseTableConfig):
    YEAR_LIST = (2017,)
    PROCESSED_TABLE_NAME = "internet"
    UNIVERSE = "households"
    RAW_TABLE_NAME = 'B28002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "internet_any_source",
        '003': "dialup_only",
        '004': "broadband_any_source",
        '005': "cellular_data",
        '006': "cellular_data_only",
        '007': "broadband_cable_fiber_or_dsl",
        '008': "broadband_only",
        '009': "satellite",
        '010': "satellite_only",
        '011': "other_only",
        '012': "internet_without_subscription",
        '013': "no_internet"
    })

    def process(self, df):
        # This field, which combines people with no internet and those only only receive via
        # a free program like municipal wifi together into a combined group.
        # The Census Bureau considers this to be the true number of households without Internet access.
        # Calculate moe for these rows so we can use in the median aggregator
        def calculate_moe(row):
            pprint(row)
            if row['internet_without_subscription_moe'] in list(MOE_MAP.values()):
                value = sum([row['internet_without_subscription'], row['no_internet']])
                moe = None
            value, moe = census_data_aggregator.approximate_sum(
                (row['internet_without_subscription'], row['internet_without_subscription_moe']),
                (row['no_internet'], row['no_internet_moe']),
            )
            row['total_no_internet_and_no_subscription'] = value
            row['total_no_internet_and_no_subscription_moe'] = moe
            return row

        df = df.apply(
            calculate_moe,
            axis=1
        )

        # Pass it back
        return df
