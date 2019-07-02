#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class YearStructureBuiltDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "yearstructurebuilt"
    UNIVERSE = "housing units"
    RAW_TABLE_NAME = 'B25034'

    @property
    def RAW_FIELD_CROSSWALK(self):
        if self._year > 2014:
            return collections.OrderedDict({
                '001': 'universe',
                '002': 'built_2014_or_later',
                '003': 'built_2010_to_2013',
                '004': 'built_2000_to_2009',
                '005': 'built_1990_to_1999',
                '006': 'built_1980_to_1989',
                '007': 'built_1970_to_1979',
                '008': 'built_1960_to_1969',
                '009': 'built_1950_to_1959',
                '010': 'built_1940_to_1949',
                '011': 'built_1929_or_earlier'
            })
        elif self._year > 2011:
            return collections.OrderedDict({
                '001': 'universe',
                '002': 'built_2010_or_later',
                '003': 'built_2000_to_2009',
                '004': 'built_1990_to_1999',
                '005': 'built_1980_to_1989',
                '006': 'built_1970_to_1979',
                '007': 'built_1960_to_1969',
                '008': 'built_1950_to_1959',
                '009': 'built_1940_to_1949',
                '010': 'built_1939_or_earlier'
            })
        else:
            return collections.OrderedDict({
                '001': 'universe',
                '002': 'built_2005_or_later',
                '003': 'built_2000_to_2004',
                '004': 'built_1990_to_1999',
                '005': 'built_1980_to_1989',
                '006': 'built_1970_to_1979',
                '007': 'built_1960_to_1969',
                '008': 'built_1950_to_1959',
                '009': 'built_1940_to_1949',
                '010': 'built_1939_or_earlier'
            })
