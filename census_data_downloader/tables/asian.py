#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class AsianDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "asian"
    UNIVERSE = "total asian alone population"
    RAW_TABLE_NAME = 'B02015'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': "universe",
        '002E': "asian_indian",
        '003E': "bangladeshi",
        '004E': "bhutanese",
        '005E': "burmese",
        '006E': "cambodian",
        '007E': "chinese_except_taiwanese",
        '008E': "filipino",
        '009E': "hmong",
        '010E': "indonesian",
        '011E': "japanese",
        '012E': "korean",
        '013E': "laotian",
        '014E': "malaysian",
        '015E': "mongolian",
        '016E': "nepalese",
        '017E': "okinawan",
        '018E': "pakistani",
        '019E': "sri_lankan",
        '020E': "taiwanese",
        '021E': "thai",
        '022E': "vietnamese",
        '023E': "other_asian_specified",
        '024E': "other_asian_not_specified",
        '025E': "two_or_more_asian",
    })
