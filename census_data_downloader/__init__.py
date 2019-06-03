#! /usr/bin/env python
# -*- coding: utf-8 -*
# flake8: NOQA
import logging
from us import states
from .registry import DOWNLOADERS
from .age import AgeDownloader
from .classofworker import ClassOfWorkerDownloader
from .education import EducationDownloader
from .employmentstatus import EmploymentStatusDownloader
from .foreignborn import ForeignBornDownloader
from .householdincome import (
    HouseholdIncomeDownloader,
    HouseholdIncomeLatinoDownloader,
    HouseholdIncomeWhiteDownloader,
    HouseholdIncomeBlackDownloader,
    HouseholdIncomeAsianDownloader
)
from .internet import InternetDownloader
from .language import (
    HouseholdLanguageDownloader,
    LanguageShortFormDownloader,
    LanguageLongFormDownloader
)
from .medianage import MedianAgeDownloader
from .mediangrossrent import MedianGrossRentDownloader
from .medianhouseholdincome import (
    MedianHouseholdIncomeDownloader,
    MedianHouseholdIncomeLatinoDownloader,
    MedianHouseholdIncomeWhiteDownloader,
    MedianHouseholdIncomeBlackDownloader,
    MedianHouseholdIncomeAsianDownloader
)
from .medianhousingvalue import MedianHousingValueDownloader
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
from .race import (
    RaceDownloader,
    AmericanIndianAlaskaNativeAloneOrInComboDownloader
)
from .tenure import (
    TenureDownloader,
    TenureLatinoDownloader,
    TenureWhiteDownloader,
    TenureBlackDownloader,
    TenureAsianDownloader
)
from .yearstructurebuilt import YearStructureBuiltDownloader
logger = logging.getLogger(__name__)


def download_everything(*args, **kwargs):
    """
    Download all the data.
    """
    logger.debug("Downloading all datasets for all geographies")
    for klass in DOWNLOADERS:
        obj = klass(*args, **kwargs)
        logger.debug(f"Downloading nationwide {klass.PROCESSED_TABLE_NAME} dataset")
        obj.download_everything()


__all__ = ("DOWNLOADERS", "download_everything")
