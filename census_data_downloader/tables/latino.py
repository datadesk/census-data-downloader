#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class LatinoDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "latino"
    UNIVERSE = "total population"
    RAW_TABLE_NAME = 'B03001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "not_hispanic_or_latino",
        '003': "hispanic_or_latino",
        '004': "mexican",
        '005': "puerto_rican",
        '006': "cuban",
        '007': "dominican",
        '008': "central_american",
        '009': "costa_rican",
        '010': "guatemalan",
        '011': "honduran",
        '012': "nicaraguan",
        '013': "panamanian",
        '014': "salvadoran",
        '015': "other_central_american",
        '016': "south_american",
        '017': "argentinean",
        '018': "bolivian",
        '019': "chilean",
        '020': "colombian",
        '021': "ecuadorian",
        '022': "paraguayan",
        '023': "peruvian",
        '024': "uruguayan",
        '025': "venezuelan",
        '026': "other_south_american",
        '027': "other_hispanic_or_latino",
        '028': "spaniard",
        '029': "spanish",
        '030': "spanish_american",
        '031': "all_other_hispanic_or_latino"
    })
