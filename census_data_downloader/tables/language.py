#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class HouseholdLanguageDownloader(BaseTableConfig):
    YEAR_LIST = (2017, 2016)
    PROCESSED_TABLE_NAME = 'householdlanguage'
    UNIVERSE = "households"
    RAW_TABLE_NAME = 'C16002'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        "001": "universe",
        "002": "only_english",
        "003": "total_spanish",
        "004": "spanish_limited_english",
        "005": "spanish_not_limited_english",
        "006": "total_other_indo_european",
        "007": "other_indo_european_limited_english",
        "008": "other_indo_european_not_limited_english",
        "009": "total_asian_and_pacific_islander",
        "010": "asian_and_pacific_islander_limited_english",
        "011": "asian_and_pacific_islander_not_limited_english",
        "012": "total_other",
        "013": "other_limited_english",
        "014": "other_not_limited_english",
    })

    def process(self, df):
        """
        Combine language counts to get total english/non-english speakers
        """
        languages = [
            'spanish',
            'other_indo_european',
            'asian_and_pacific_islander',
            'other'
        ]

        # English vs. no English totals
        df['total_not_limited_english'] = df['only_english'] + df[[f'{l}_not_limited_english' for l in languages]].sum(axis=1)
        df['total_limited_english'] = df[[f'{l}_limited_english' for l in languages]].sum(axis=1)

        # Pass it out
        return df


@register
class LanguageShortFormDownloader(BaseTableConfig):
    YEAR_LIST = (2017, 2016)
    PROCESSED_TABLE_NAME = 'languageshortform'
    UNIVERSE = "population 5 years and over"
    RAW_TABLE_NAME = 'C16001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': 'universe',
        '002': 'only_english',
        '003': 'total_spanish',
        '004': 'spanish_and_english_very_well',
        '005': 'spanish_and_english_less_than_very_well',
        '006': 'total_french_haitan_or_cajun',
        '007': 'french_haitan_or_cajun_and_english_very_well',
        '008': 'french_haitan_or_cajun_and_english_less_than_very_well',
        '009': 'total_german_or_other_west_germanic',
        '010': 'german_or_other_west_germanic_and_english_very_well',
        '011': 'german_or_other_west_germanic_and_english_less_than_very_well',
        '012': 'total_russian_polish_or_other_slavic',
        '013': 'russian_polish_or_other_slavic_and_english_very_well',
        '014': 'russian_polish_or_other_slavic_and_english_less_than_very_well',
        '015': 'total_other_indo_european',
        '016': 'other_indo_european_and_english_very_well',
        '017': 'other_indo_european_and_english_less_than_very_well',
        '018': 'total_korean',
        '019': 'korean_and_english_very_well',
        '020': 'korean_and_english_less_than_very_well',
        '021': 'total_chinese',
        '022': 'chinese_and_english_very_well',
        '023': 'chinese_and_english_less_than_very_well',
        '024': 'total_vietnamese',
        '025': 'vietnamese_and_english_very_well',
        '026': 'vietnamese_and_english_less_than_very_well',
        '027': 'total_tagalog',
        '028': 'tagalog_and_english_very_well',
        '029': 'tagalog_and_english_less_than_very_well',
        '030': 'total_other_asian',
        '031': 'other_asian_and_english_very_well',
        '032': 'other_asian_and_english_less_than_very_well',
        '033': 'total_arabic',
        '034': 'arabic_and_english_very_well',
        '035': 'arabic_and_english_less_than_very_well',
        '036': 'total_other',
        '037': 'other_and_english_very_well',
        '038': 'other_and_english_less_than_very_well'
    })

    def process(self, df):
        """
        Combine language counts to get total english/non-english speakers
        """
        languages = [
            'spanish',
            'french_haitan_or_cajun',
            'german_or_other_west_germanic',
            'russian_polish_or_other_slavic',
            'other_indo_european',
            'korean',
            'chinese',
            'vietnamese',
            'tagalog',
            'other_asian',
            'arabic',
            'other'
        ]

        # English vs. no English totals
        df['total_english'] = df['only_english'] + df[
            [f'{l}_and_english_very_well' for l in languages]
        ].sum(axis=1)
        df['total_english_less_than_very_well'] = df[
            [f'{l}_and_english_less_than_very_well' for l in languages]
        ].sum(axis=1)

        # Pass it out
        return df


@register
class LanguageLongFormDownloader(BaseTableConfig):
    YEAR_LIST = (2017, 2016)
    GEOTYPE_LIST = ("nationwide", "states", "counties", "congressional_districts", "places")
    PROCESSED_TABLE_NAME = 'languagelongform'
    UNIVERSE = "population 5 years and over"
    RAW_TABLE_NAME = 'B16001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': 'universe',
        '002': 'only_english',
        '003': 'total_spanish',
        '004': 'spanish_and_english_very_well',
        '005': 'spanish_and_english_less_than_very_well',
        '006': 'total_french',
        '007': 'french_and_english_very_well',
        '008': 'french_and_english_less_than_very_well',
        '009': 'total_haitian',
        '010': 'haitian_and_english_very_well',
        '011': 'haitian_and_english_less_than_very_well',
        '012': 'total_italian',
        '013': 'italian_and_english_very_well',
        '014': 'italian_and_english_less_than_very_well',
        '015': 'total_portuguese',
        '016': 'portuguese_and_english_very_well',
        '017': 'portuguese_and_english_less_than_very_well',
        '018': 'total_german',
        '019': 'german_and_english_very_well',
        '020': 'german_and_english_less_than_very_well',
        '021': 'total_other_germanic',
        '022': 'other_germanic_and_english_very_well',
        '023': 'other_germanic_and_english_less_than_very_well',
        '024': 'total_greek',
        '025': 'greek_and_english_very_well',
        '026': 'greek_and_english_less_than_very_well',
        '027': 'total_russian',
        '028': 'russian_and_english_very_well',
        '029': 'russian_and_english_less_than_very_well',
        '030': 'total_polish',
        '031': 'polish_and_english_very_well',
        '032': 'polish_and_english_less_than_very_well',
        '033': 'total_serbo_croatian',
        '034': 'serbo_croatian_and_english_very_well',
        '035': 'serbo_croatian_and_english_less_than_very_well',
        '036': 'total_other_slavic',
        '037': 'other_slavic_and_english_very_well',
        '038': 'other_slavic_and_english_less_than_very_well',
        '039': 'total_armenian',
        '040': 'armenian_and_english_very_well',
        '041': 'armenian_and_english_less_than_very_well',
        '042': 'total_persian',
        '043': 'persian_and_english_very_well',
        '044': 'persian_and_english_less_than_very_well',
        '045': 'total_gujarati',
        '046': 'gujarati_and_english_very_well',
        '047': 'gujarati_and_english_less_than_very_well',
        '048': 'total_hindi',
        '049': 'hindi_and_english_very_well',
        '050': 'hindi_and_english_less_than_very_well',
        '051': 'total_urdu',
        '052': 'urdu_and_english_very_well',
        '053': 'urdu_and_english_less_than_very_well',
        '054': 'total_punjabi',
        '055': 'punjabi_and_english_very_well',
        '056': 'punjabi_and_english_less_than_very_well',
        '057': 'total_bengali',
        '058': 'bengali_and_english_very_well',
        '059': 'bengali_and_english_less_than_very_well',
        '060': 'total_other_indic',
        '061': 'other_indic_and_english_very_well',
        '062': 'other_indic_and_english_less_than_very_well',
        '063': 'total_other_indoeuropean',
        '064': 'other_indoeuropean_and_english_very_well',
        '065': 'other_indoeuropean_and_english_less_than_very_well',
        '066': 'total_telugu',
        '067': 'telugu_and_english_very_well',
        '068': 'telugu_and_english_less_than_very_well',
        '069': 'total_tamil',
        '070': 'tamil_and_english_very_well',
        '071': 'tamil_and_english_less_than_very_well',
        '072': 'total_other_dravidian',
        '073': 'other_dravidian_and_english_very_well',
        '074': 'other_dravidian_and_english_less_than_very_well',
        '075': 'total_chinese',
        '076': 'chinese_and_english_very_well',
        '077': 'chinese_and_english_less_than_very_well',
        '078': 'total_japanese',
        '079': 'japanese_and_english_very_well',
        '080': 'japanese_and_english_less_than_very_well',
        '081': 'total_korean',
        '082': 'korean_and_english_very_well',
        '083': 'korean_and_english_less_than_very_well',
        '084': 'total_hmong',
        '085': 'hmong_and_english_very_well',
        '086': 'hmong_and_english_less_than_very_well',
        '087': 'total_vietnamese',
        '088': 'vietnamese_and_english_very_well',
        '089': 'vietnamese_and_english_less_than_very_well',
        '090': 'total_khmer',
        '091': 'khmer_and_english_very_well',
        '092': 'khmer_and_english_less_than_very_well',
        '093': 'total_other_tai_kadai',
        '094': 'other_tai_kadai_and_english_very_well',
        '095': 'other_tai_kadai_and_english_less_than_very_well',
        '096': 'total_other_asia',
        '097': 'other_asia_and_english_very_well',
        '098': 'other_asia_and_english_less_than_very_well',
        '099': 'total_tagalog',
        '100': 'tagalog_and_english_very_well',
        '101': 'tagalog_and_english_less_than_very_well',
        '102': 'total_other_austronesian',
        '103': 'other_austronesian_and_english_very_well',
        '104': 'other_austronesian_and_english_less_than_very_well',
        '105': 'total_arabic',
        '106': 'arabic_and_english_very_well',
        '107': 'arabic_and_english_less_than_very_well',
        '108': 'total_hebrew',
        '109': 'hebrew_and_english_very_well',
        '110': 'hebrew_and_english_less_than_very_well',
        '111': 'total_other_afroasiatic',
        '112': 'other_afroasiatic_and_english_very_well',
        '113': 'other_afroasiatic_and_english_less_than_very_well',
        '114': 'total_other_western_africa',
        '115': 'other_western_africa_and_english_very_well',
        '116': 'other_western_africa_and_english_less_than_very_well',
        '117': 'total_other_central_eastern_southern_africa',
        '118': 'other_central_eastern_southern_africa_and_english_very_well',
        '119': 'other_central_eastern_southern_africa_and_english_less_than_very_well',
        '120': 'total_navajo',
        '121': 'navajo_and_english_very_well',
        '122': 'navajo_and_english_less_than_very_well',
        '123': 'total_other_native_north_america',
        '124': 'other_native_north_america_and_english_very_well',
        '125': 'other_native_north_america_and_english_less_than_very_well',
        '126': 'total_other_unspecified',
        '127': 'other_unspecified_and_english_very_well',
        '128': 'other_unspecified_and_english_less_than_very_well'
    })

    def process(self, df):
        """
        Combine language counts to get total english/non-english speakers
        """
        languages = [
            'spanish',
            'french',
            'haitian',
            'italian',
            'portuguese',
            'german',
            'other_germanic',
            'greek',
            'russian',
            'polish',
            'serbo_croatian',
            'other_slavic',
            'armenian',
            'persian',
            'gujarati',
            'hindi',
            'urdu',
            'punjabi',
            'bengali',
            'other_indic',
            'other_indoeuropean',
            'telugu',
            'tamil',
            'other_dravidian',
            'chinese',
            'japanese',
            'korean',
            'hmong',
            'vietnamese',
            'khmer',
            'other_tai_kadai',
            'other_asia',
            'tagalog',
            'other_austronesian',
            'arabic',
            'hebrew',
            'other_afroasiatic',
            'other_western_africa',
            'other_central_eastern_southern_africa',
            'navajo',
            'other_native_north_america',
            'other_unspecified'
        ]

        # English vs. no English totals
        df['total_english'] = df['only_english'] + df[[f'{l}_and_english_very_well' for l in languages]].sum(axis=1)
        df['total_english_less_than_very_well'] = df[
            [f'{l}_and_english_less_than_very_well' for l in languages]
        ].sum(axis=1)

        # Group into the four language groups defined by the Census
        # https://www.census.gov/topics/population/language-use/about.html
        # Calculate our custom groups (other than Spanish, which we already have)
        groupsets = collections.OrderedDict({
            "other_indo_european_group": [
                'french',
                'haitian',
                'italian',
                'portuguese',
                'german',
                'other_germanic',
                'greek',
                'russian',
                'polish',
                'serbo_croatian',
                'other_slavic',
                'armenian',
                'persian',
                'gujarati',
                'hindi',
                'urdu',
                'punjabi',
                'bengali',
                'other_indic',
                'other_indoeuropean',
                'telugu',
                'tamil',
                'other_dravidian'
            ],
            "asian_and_pacific_island_group": [
                'chinese',
                'japanese',
                'korean',
                'hmong',
                'vietnamese',
                'khmer',
                'other_tai_kadai',
                'other_asia',
                'tagalog',
                'other_austronesian'
            ],
            "all_other_group": [
                'arabic',
                'hebrew',
                'other_afroasiatic',
                'other_western_africa',
                'other_central_eastern_southern_africa',
                'navajo',
                'other_native_north_america',
                'other_unspecified'
            ]
        })
        for groupset, group_list in groupsets.items():
            df[f'total_{groupset}'] = df[
                [f'total_{f}' for f in group_list]
            ].sum(axis=1)
            df[f'{groupset}_and_english_very_well'] = df[
                [f'{f}_and_english_very_well' for f in group_list]
            ].sum(axis=1)
            df[f'{groupset}_and_english_less_than_very_well'] = df[
                [f'{f}_and_english_less_than_very_well' for f in group_list]
            ].sum(axis=1)

        # Pass it back
        return df
