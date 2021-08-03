#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class OccupantsDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "occupants"
    UNIVERSE = "occupied housing unts"
    RAW_TABLE_NAME = "B25014"
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "owner_occupied",
        '003': "owner_occupied_050_or_less",
        '004': "owner_occupied_051_to_100",
        '005': "owner_occupied_101_to_150",
        '006': "owner_occupied_151_to_200",
        '007': "owner_occupied_201_or_more",
        '008': "renter_occupied",
        '009': "renter_occupied_050_or_less",
        '010': "renter_occupied_051_to_100",
        '011': "renter_occupied_101_to_150",
        '012': "renter_occupied_151_to_200",
        '013': "renter_occupied_201_or_more"
    })
