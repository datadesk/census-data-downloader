#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register

@register
class LatinoDownloader(BaseTableConfig):
    PROCESSED_TABLE_NAME = "singleancestry"
    UNIVERSE = "people reporting single ancestry"
    RAW_TABLE_NAME = 'B04004'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
	    '001E': "universe",
        '002E': "afghan",
        '003E': "albanian",
        '004E': "alsatian",
        '005E': "american",
        '006E': "arab",
        '007E': "egyptian",
        '008E': "iraqi",
        '009E': "jordanian",
        '010E': "lebanese",
        '011E': "moroccan",
        '012E': "palestinian",
        '013E': "syrian",
        '014E': "all_arab",
        '015E': "other_arab",
        '016E': "armenian",
        '017E': "assyrian/chaldean/syriac",
        '018E': "australian",
        '019E': "austrian",
        '020E': "basque",
        '021E': "belgian",
        '022E': "brazilian",
        '023E': "british",
        '024E': "bulgarian",
        '025E': "cajun",
        '026E': "canadian",
        '027E': "carpatho_rusyn",
        '028E': "celtic",
        '029E': "croatian",
        '030E': "cypriot",
        '031E': "czech",
        '032E': "czechoslovakian"
    })
