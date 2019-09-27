from census_data_downloader.core.decorators import TABLE_LIST
from .age import AgeDownloader
from .ancestry import AncestryDownloader
from .classofworker import ClassOfWorkerDownloader
from .disability import (
    DisabilityDownloader,
    DisabilityPovertyDownloader
)
from .education import EducationDownloader
from .employmentstatus import EmploymentStatusDownloader
from .foreignborn import (
    ForeignBornDownloader,
    CitizenDownloader
)
from .gini import GiniIndexDownloader
from .housing import (
    MedianMonthlyHousingCostsDownloader,
    MedianHousingValueDownloader,
    MedianGrossRentDownloader,
    TenureDownloader,
    TenureLatinoDownloader,
    TenureWhiteDownloader,
    TenureBlackDownloader,
    TenureAsianDownloader
)
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
from .latino import LatinoDownloader
from .medianage import MedianAgeDownloader
from .medianhouseholdincome import (
    MedianHouseholdIncomeDownloader,
    MedianHouseholdIncomeLatinoDownloader,
    MedianHouseholdIncomeWhiteDownloader,
    MedianHouseholdIncomeBlackDownloader,
    MedianHouseholdIncomeAsianDownloader
)
from .mobility import (
    MobilityDownloader,
    MobilityBySexDownloader,
    MobilityWhiteDownloader,
    MobilityBlackDownloader,
    MobilityAsianDownloader,
    MobilityLatinoDownloader,
    MobilityByCitizenship
)
from .percapitaincome import (
    PerCapitaIncomeDownloader,
    PerCapitaIncomeLatinoDownloader,
    PerCapitaIncomeWhiteDownloader,
    PerCapitaIncomeBlackDownloader,
    PerCapitaIncomeAsianDownloader
)
from .population import PopulationDownloader
from .poverty import (
    PovertyDownloader,
    PovertyBySexDownloader,
    PovertyAgeDownloader,
    PovertyLatinoDownloader,
    PovertyWhiteDownloader,
    PovertyBlackDownloader,
    PovertyAsianDownloader
)
from .race import (
    RaceDownloader,
    AmericanIndianAlaskaNativeAloneOrInComboDownloader,
    AsianDownloader
)
from .snap import (
    SnapbyPovertyDownloader,
    SnapLatinoDownloader,
    SnapWhiteDownloader,
    SnapBlackDownloader,
    SnapAsianDownloader,
)
from .yearstructurebuilt import YearStructureBuiltDownloader

__all__ = [
    TABLE_LIST,
    AgeDownloader,
    AncestryDownloader,
    AsianDownloader,
    CitizenDownloader,
    ClassOfWorkerDownloader,
    DisabilityDownloader,
    DisabilityPovertyDownloader,
    EducationDownloader,
    EmploymentStatusDownloader,
    ForeignBornDownloader,
    GiniIndexDownloader,
    HouseholdIncomeDownloader,
    HouseholdIncomeLatinoDownloader,
    HouseholdIncomeWhiteDownloader,
    HouseholdIncomeBlackDownloader,
    HouseholdIncomeAsianDownloader,
    InternetDownloader,
    HouseholdLanguageDownloader,
    LanguageShortFormDownloader,
    LanguageLongFormDownloader,
    LatinoDownloader,
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
    MobilityByCitizenship,
    PerCapitaIncomeDownloader,
    PerCapitaIncomeLatinoDownloader,
    PerCapitaIncomeWhiteDownloader,
    PerCapitaIncomeBlackDownloader,
    PerCapitaIncomeAsianDownloader,
    PopulationDownloader,
    PovertyDownloader,
    PovertyBySexDownloader,
    PovertyAgeDownloader,
    PovertyLatinoDownloader,
    PovertyWhiteDownloader,
    PovertyBlackDownloader,
    PovertyAsianDownloader,
    RaceDownloader,
    SnapbyPovertyDownloader,
    SnapLatinoDownloader,
    SnapWhiteDownloader,
    SnapBlackDownloader,
    SnapAsianDownloader,
    AmericanIndianAlaskaNativeAloneOrInComboDownloader,
    TenureDownloader,
    TenureLatinoDownloader,
    TenureWhiteDownloader,
    TenureBlackDownloader,
    TenureAsianDownloader,
    YearStructureBuiltDownloader
]
