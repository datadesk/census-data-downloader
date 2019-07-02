#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class InternetDownloader(BaseTableConfig):
    YEAR_LIST = (2017,)
    PROCESSED_TABLE_NAME = "internet"
    UNIVERSE = "households"
    RAW_TABLE_NAME = 'B28002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': "universe",
        '002E': "internet_any_source",
        '003E': "dialup_only",
        '004E': "broadband_any_source",
        '005E': "cellular_data",
        '006E': "cellular_data_only",
        '007E': "broadband_cable_fiber_or_dsl",
        '008E': "broadband_only",
        '009E': "satellite",
        '010E': "satellite_only",
        '011E': "other_only",
        '012E': "internet_without_subscription",
        '013E': "no_internet"
    })

    def process(self, *args, **kwargs):
        df = super().process(*args, **kwargs)

        # This field, which combines people with no internet and those only only receive via
        # a free program like municipal wifi together into a combined group.
        # The Census Bureau considers this to be the true number of households without Internet access.
        df['total_no_internet_and_no_subscription'] = df['internet_without_subscription'] + df['no_internet']

        # Pass it back
        return df
