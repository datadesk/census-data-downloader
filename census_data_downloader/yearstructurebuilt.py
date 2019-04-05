#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class YearStructureBuiltDownloader(BaseDownloader):
    PROCESSED_TABLE_NAME = "yearstructurebuilt"
    RAW_TABLE_NAME = 'B25034'

    @property
    def RAW_FIELD_CROSSWALK(self):
        if self._year > 2014:
            return collections.OrderedDict({
                '001E': 'housing_units',
                '002E': 'built_2014_or_later',
                '003E': 'built_2010_to_2013',
                '004E': 'built_2000_to_2009',
                '005E': 'built_1990_to_1999',
                '006E': 'built_1980_to_1989',
                '007E': 'built_1970_to_1979',
                '008E': 'built_1960_to_1969',
                '009E': 'built_1950_to_1959',
                '010E': 'built_1940_to_1949',
                '011E': 'built_1929_or_earlier'
            })
        elif self._year > 2011:
            return collections.OrderedDict({
                '001E': 'housing_units',
                '002E': 'built_2010_or_later',
                '003E': 'built_2000_to_2009',
                '004E': 'built_1990_to_1999',
                '005E': 'built_1980_to_1989',
                '006E': 'built_1970_to_1979',
                '007E': 'built_1960_to_1969',
                '008E': 'built_1950_to_1959',
                '009E': 'built_1940_to_1949',
                '010E': 'built_1939_or_earlier'
            })
        else:
            return collections.OrderedDict({
                '001E': 'housing_units',
                '002E': 'built_2005_or_later',
                '003E': 'built_2000_to_2004',
                '004E': 'built_1990_to_1999',
                '005E': 'built_1980_to_1989',
                '006E': 'built_1970_to_1979',
                '007E': 'built_1960_to_1969',
                '008E': 'built_1950_to_1959',
                '009E': 'built_1940_to_1949',
                '010E': 'built_1939_or_earlier'
            })
