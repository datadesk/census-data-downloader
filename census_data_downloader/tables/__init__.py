from census_data_downloader.core.decorators import TABLE_LIST
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
from .poverty import PovertyDownloader
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
# from .yearstructurebuilt import YearStructureBuiltDownloader

__all__ = [
    TABLE_LIST,
    AgeDownloader,
    ClassOfWorkerDownloader,
    EducationDownloader,
    EmploymentStatusDownloader,
    ForeignBornDownloader,
    HouseholdIncomeDownloader,
    HouseholdIncomeLatinoDownloader,
    HouseholdIncomeWhiteDownloader,
    HouseholdIncomeBlackDownloader,
    HouseholdIncomeAsianDownloader,
    InternetDownloader,
    HouseholdLanguageDownloader,
    LanguageShortFormDownloader,
    LanguageLongFormDownloader,
    MedianAgeDownloader,
    MedianGrossRentDownloader,
    MedianHouseholdIncomeDownloader,
    MedianHouseholdIncomeLatinoDownloader,
    MedianHouseholdIncomeWhiteDownloader,
    MedianHouseholdIncomeBlackDownloader,
    MedianHouseholdIncomeAsianDownloader,
    MedianHousingValueDownloader,
    MedianMonthlyHousingCostsDownloader,
    MobilityDownloader,
    MobilityBySexDownloader,
    MobilityWhiteDownloader,
    MobilityBlackDownloader,
    MobilityAsianDownloader,
    MobilityLatinoDownloader,
    PopulationDownloader,
    PovertyDownloader,
    RaceDownloader,
    AmericanIndianAlaskaNativeAloneOrInComboDownloader,
    TenureDownloader,
    TenureLatinoDownloader,
    TenureWhiteDownloader,
    TenureBlackDownloader,
    TenureAsianDownloader
]
