#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from .base import BaseDownloader
from .registry import register_downloader


@register_downloader
class LanguageDownloader(BaseDownloader):
    YEAR_LIST = (2017, 2016)
    PROCESSED_TABLE_NAME = 'language'
    RAW_TABLE_NAME = 'B16001'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001E': 'total',
        '002E': 'only_english',
        '003E': 'total_spanish',
        '004E': 'spanish_and_english_very_well',
        '005E': 'spanish_and_english_less_than_very_well',
        '006E': 'total_french',
        '007E': 'french_and_english_very_well',
        '008E': 'french_and_english_less_than_very_well',
        '009E': 'total_haitian',
        '010E': 'haitian_and_english_very_well',
        '011E': 'haitian_and_english_less_than_very_well',
        '012E': 'total_italian',
        '013E': 'italian_and_english_very_well',
        '014E': 'italian_and_english_less_than_very_well',
        '015E': 'total_portuguese',
        '016E': 'portuguese_and_english_very_well',
        '017E': 'portuguese_and_english_less_than_very_well',
        '018E': 'total_german',
        '019E': 'german_and_english_very_well',
        '020E': 'german_and_english_less_than_very_well',
        '021E': 'total_other_germanic',
        '022E': 'other_germanic_and_english_very_well',
        '023E': 'other_germanic_and_english_less_than_very_well',
        '024E': 'total_greek',
        '025E': 'greek_and_english_very_well',
        '026E': 'greek_and_english_less_than_very_well',
        '027E': 'total_russian',
        '028E': 'russian_and_english_very_well',
        '029E': 'russian_and_english_less_than_very_well',
        '030E': 'total_polish',
        '031E': 'polish_and_english_very_well',
        '032E': 'polish_and_english_less_than_very_well',
        '033E': 'total_serbo_croatian',
        '034E': 'serbo_croatian_and_english_very_well',
        '035E': 'serbo_croatian_and_english_less_than_very_well',
        '036E': 'total_other_slavic',
        '037E': 'other_slavic_and_english_very_well',
        '038E': 'other_slavic_and_english_less_than_very_well',
        '039E': 'total_armenian',
        '040E': 'armenian_and_english_very_well',
        '041E': 'armenian_and_english_less_than_very_well',
        '042E': 'total_persian',
        '043E': 'persian_and_english_very_well',
        '044E': 'persian_and_english_less_than_very_well',
        '045E': 'total_gujarati',
        '046E': 'gujarati_and_english_very_well',
        '047E': 'gujarati_and_english_less_than_very_well',
        '048E': 'total_hindi',
        '049E': 'hindi_and_english_very_well',
        '050E': 'hindi_and_english_less_than_very_well',
        '051E': 'total_urdu',
        '052E': 'urdu_and_english_very_well',
        '053E': 'urdu_and_english_less_than_very_well',
        '054E': 'total_punjabi',
        '055E': 'punjabi_and_english_very_well',
        '056E': 'punjabi_and_english_less_than_very_well',
        '057E': 'total_bengali',
        '058E': 'bengali_and_english_very_well',
        '059E': 'bengali_and_english_less_than_very_well',
        '060E': 'total_other_indic',
        '061E': 'other_indic_and_english_very_well',
        '062E': 'other_indic_and_english_less_than_very_well',
        '063E': 'total_other_indoeuropean',
        '064E': 'other_indoeuropean_and_english_very_well',
        '065E': 'other_indoeuropean_and_english_less_than_very_well',
        '066E': 'total_telugu',
        '067E': 'telugu_and_english_very_well',
        '068E': 'telugu_and_english_less_than_very_well',
        '069E': 'total_tamil',
        '070E': 'tamil_and_english_very_well',
        '071E': 'tamil_and_english_less_than_very_well',
        '072E': 'total_other_dravidian',
        '073E': 'other_dravidian_and_english_very_well',
        '074E': 'other_dravidian_and_english_less_than_very_well',
        '075E': 'total_chinese',
        '076E': 'chinese_and_english_very_well',
        '077E': 'chinese_and_english_less_than_very_well',
        '078E': 'total_japanese',
        '079E': 'japanese_and_english_very_well',
        '080E': 'japanese_and_english_less_than_very_well',
        '081E': 'total_korean',
        '082E': 'korean_and_english_very_well',
        '083E': 'korean_and_english_less_than_very_well',
        '084E': 'total_hmong',
        '085E': 'hmong_and_english_very_well',
        '086E': 'hmong_and_english_less_than_very_well',
        '087E': 'total_vietnamese',
        '088E': 'vietnamese_and_english_very_well',
        '089E': 'vietnamese_and_english_less_than_very_well',
        '090E': 'total_khmer',
        '091E': 'khmer_and_english_very_well',
        '092E': 'khmer_and_english_less_than_very_well',
        '093E': 'total_other_tai_kadai',
        '094E': 'other_tai_kadai_and_english_very_well',
        '095E': 'other_tai_kadai_and_english_less_than_very_well',
        '096E': 'total_other_asia',
        '097E': 'other_asia_and_english_very_well',
        '098E': 'other_asia_and_english_less_than_very_well',
        '099E': 'total_tagalog',
        '100E': 'tagalog_and_english_very_well',
        '101E': 'tagalog_and_english_less_than_very_well',
        '102E': 'total_other_austronesian',
        '103E': 'other_austronesian_and_english_very_well',
        '104E': 'other_austronesian_and_english_less_than_very_well',
        '105E': 'total_arabic',
        '106E': 'arabic_and_english_very_well',
        '107E': 'arabic_and_english_less_than_very_well',
        '108E': 'total_hebrew',
        '109E': 'hebrew_and_english_very_well',
        '110E': 'hebrew_and_english_less_than_very_well',
        '111E': 'total_other_afroasiatic',
        '112E': 'other_afroasiatic_and_english_very_well',
        '113E': 'other_afroasiatic_and_english_less_than_very_well',
        '114E': 'total_other_western_africa',
        '115E': 'other_western_africa_and_english_very_well',
        '116E': 'other_western_africa_and_english_less_than_very_well',
        '117E': 'total_other_central_eastern_southern_africa',
        '118E': 'other_central_eastern_southern_africa_and_english_very_well',
        '119E': 'other_central_eastern_southern_africa_and_english_less_than_very_well',
        '120E': 'total_navajo',
        '121E': 'navajo_and_english_very_well',
        '122E': 'navajo_and_english_less_than_very_well',
        '123E': 'total_other_native_north_america',
        '124E': 'other_native_north_america_and_english_very_well',
        '125E': 'other_native_north_america_and_english_less_than_very_well',
        '126E': 'total_other_unspecified',
        '127E': 'other_unspecified_and_english_very_well',
        '128E': 'other_unspecified_and_english_less_than_very_well'
    })

    def _process_raw_data(self, *args, **kwargs):
        """
        Combine language counts to get total english/non-english speakers
        """
        df = super()._process_raw_data(*args, **kwargs)

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
