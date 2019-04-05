#! /usr/bin/env python
# -*- coding: utf-8 -*
# flake8: NOQA
import logging
from us import states
from .registry import DOWNLOADERS
from .age import AgeDownloader
from .education import EducationDownloader
from .foreignborn import ForeignBornDownloader
from .householdincome import (
    HouseholdIncomeDownloader,
    HouseholdIncomeLatinoDownloader,
    HouseholdIncomeWhiteDownloader,
    HouseholdIncomeBlackDownloader,
    HouseholdIncomeAsianDownloader
)
from .internet import InternetDownloader
from .medianage import MedianAgeDownloader
from .medianhouseholdincome import (
    MedianHouseholdIncomeDownloader,
    MedianHouseholdIncomeLatinoDownloader,
    MedianHouseholdIncomeWhiteDownloader,
    MedianHouseholdIncomeBlackDownloader,
    MedianHouseholdIncomeAsianDownloader
)
from .medianmonthlyhousingcosts import MedianMonthlyHousingCostsDownloader
from .mobility import (
    MobilityDownloader,
    MobilityBySexDownloader,
    MobilityWhiteDownloader,
    MobilityBlackDownloader,
    MobilityAsianDownloader,
    MobilityLatinoDownloader
)
from .population import PopulationDownloader
from .race import RaceDownloader
from .tenure import (
    TenureDownloader,
    TenureLatinoDownloader,
    TenureWhiteDownloader,
    TenureBlackDownloader,
    TenureAsianDownloader
)
from .yearstructurebuilt import YearStructureBuiltDownloader
logger = logging.getLogger(__name__)


def download_usa(*args, **kwargs):
    """
    Download all the nationwide data.
    """
    logger.debug("Downloading all datasets for all nationwide geographies")
    for klass in DOWNLOADERS:
        obj = klass(*args, **kwargs)
        logger.debug(f"Downloading nationwide {klass.PROCESSED_TABLE_NAME} datasets")
        obj.download_usa()


def download_everything(*args, **kwargs):
    """
    Download all the data.
    """
    logger.debug("Downloading all datasets for all geographies")
    for klass in DOWNLOADERS:
        obj = klass(*args, **kwargs)
        logger.debug(f"Downloading nationwide {klass.PROCESSED_TABLE_NAME} dataset")
        obj.download_usa()
        for state in states.STATES:
            logger.debug(f"Downloading tract-level {klass.PROCESSED_TABLE_NAME} data in {state.name}")
            obj.download_tracts(state.abbr)
            logger.debug(f"Downloading legislative-district-level {klass.PROCESSED_TABLE_NAME} data in {state.name}")
            obj.download_legislative_districts_upper(state.abbr)
            obj.download_legislative_districts_upper(state.abbr)


__all__ = ("DOWNLOADERS", "download_usa", "download_everything")
