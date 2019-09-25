#! /usr/bin/env python
# -*- coding: utf-8 -*
import collections
from census_data_downloader.core.tables import BaseTableConfig
from census_data_downloader.core.decorators import register


@register
class DisabilityDownloader(BaseTableConfig):
    """
    Sex by age by disability status.
    https://factfinder.census.gov/help/en/civilian_noninstitutionalized_population.htm
    """
    PROCESSED_TABLE_NAME = "disability"
    UNIVERSE = "civilian noninstitutionalized population"
    RAW_TABLE_NAME = 'B18101'
    RAW_FIELD_CROSSWALK = collections.OrderedDict({
        '001': "universe",
        '002': "male",
        '003': "male_under_5",
        '004': "male_under5_disability",
        '005': "male_under5_nodisability",
        '006': "male_5to17",
        '007': "male_5to17_disability",
        '008': "male_5to17_nodisability",
        '009': "male_18to34",
        '010': "male_18to34_disability",
        '011': "male_18to34_nodisability",
        '012': "male_35to64",
        '013': "male_35to64_disability",
        '014': "male_35to64_nodisability",
        '015': "male_65to74",
        '016': "male_65to74_disability",
        '017': "male_65to74_nodisability",
        '018': "male_75older",
        '019': "male_75older_disability",
        '020': "male_75older_nodisability",
        '021': "female",
        '022': "female_under_5",
        '023': "female_under5_disability",
        '024': "female_under5_nodisability",
        '025': "female_5to17",
        '026': "female_5to17_disability",
        '027': "female_5to17_nodisability",
        '028': "female_18to34",
        '029': "female_18to34_disability",
        '030': "female_18to34_nodisability",
        '031': "female_35to64",
        '032': "female_35to64_disability",
        '033': "female_35to64_nodisability",
        '034': "female_65to74",
        '035': "female_65to74_disability",
        '036': "female_65to74_nodisability",
        '037': "female_75older",
        '038': "female_75older_disability",
        '039': "female_75older_nodisability",
    })
