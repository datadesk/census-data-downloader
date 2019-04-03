#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader


class LanguageDownloader(BaseDownloader):
    YEAR_LIST = (2017, 2016)
    PROCESSED_TABLE_NAME = 'language'
    RAW_TABLE_NAME = 'C16001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'total',
        '002E': 'only_english',
        '004E': 'spanish_and_english',
        '005E': 'spanish_no_english',
        '007E': 'french_and_english',
        '008E': 'french_no_english',
        '010E': 'germanic_and_english',
        '011E': 'germanic_no_english',
        '013E': 'slavic_and_english',
        '014E': 'slavic_no_english',
        '016E': 'other_indoeuropean_and_english',
        '017E': 'other_indoeuropean_no_english',
        '019E': 'korean_and_english',
        '020E': 'korean_no_english',
        '022E': 'chinese_and_english',
        '023E': 'chinese_no_english',
        '025E': 'vietnamese_and_english',
        '026E': 'vietnamese_no_english',
        '028E': 'tagalog_and_english',
        '029E': 'tagalog_no_english',
        '031E': 'other_asian_and_english',
        '032E': 'other_asian_no_english',
        '034E': 'arabic_and_english',
        '035E': 'arabic_no_english',
        '037E': 'other_and_english',
        '038E': 'other_no_english'
    })

    def _process_raw_data(self, *args, **kwargs):
        """
        Combine language counts to get total english/non-english speakers
        """
        df = super()._process_raw_data(*args, **kwargs)

        languages = [
            'spanish',
            'french',
            'germanic',
            'slavic',
            'other_indoeuropean',
            'korean',
            'chinese',
            'vietnamese',
            'tagalog',
            'other_asian',
            'arabic',
            'other'
        ]
        
        df[f'total_english'] = df['only_english'] + df[[f'{l}_and_english' for l in languages]].sum(axis=1)
        df[f'total_no_english'] = df[[f'{l}_no_english' for l in languages]].sum(axis=1)

        return df
