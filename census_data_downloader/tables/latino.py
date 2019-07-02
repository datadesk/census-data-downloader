#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class LatinoDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "latinobyorigin"
    UNIVERSE = "total population"
    RAW_TABLE_NAME = 'B03001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': "universe",
        '002E': "not_hispanic_or_latino",
        '003E': "hispanic_or_latino",
        '004E': "mexican",
        '005E': "puerto_rican",
        '006E': "cuban",
        '007E': "dominican",
        '008E': "central_american",
        '009E': "costa_rican",
        '010E': "guatemalan",
        '011E': "honduran",
        '012E': "nicaraguan",
        '013E': "panamanian",
        '014E': "salvadoran",
        '015E': "other_central_american",
        '016E': "south_american",
        '017E': "argentinean",
        '018E': "bolivian",
        '019E': "chilean",
        '020E': "colombian",
        '021E': "ecuadorian",
        '022E': "paraguayan",
        '023E': "peruvian",
        '024E': "uruguayan",
        '025E': "venezuelan",
        '026E': "other_south_american",
        '027E': "other_hispanic_or_latino",
        '028E': "spaniard",
        '029E': "spanish",
        '030E': "spanish_american",
        '031E': "all_other_hispanic_or_latino"
    })
