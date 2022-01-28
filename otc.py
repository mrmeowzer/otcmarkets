# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = otc_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Auditor:
    zip: Optional[int] = None
    id: Optional[int] = None
    type: Optional[str] = None
    type_id: Optional[int] = None
    type_name: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    country_id: Optional[str] = None
    country: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state_id: Optional[str] = None
    roles: Optional[List[str]] = None
    is_public: Optional[bool] = None
    has_logo: Optional[bool] = None
    is_good_standing: Optional[bool] = None
    is_prohibited: Optional[bool] = None
    is_questionable: Optional[bool] = None
    is_attorney: Optional[bool] = None
    is_sponsor: Optional[bool] = None
    public: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Auditor':
        assert isinstance(obj, dict)
        zip = from_union([from_none, lambda x: int(from_str(x))], obj.get("zip"))
        id = from_union([from_int, from_none], obj.get("id"))
        type = from_union([from_str, from_none], obj.get("type"))
        type_id = from_union([from_int, from_none], obj.get("typeId"))
        type_name = from_union([from_str, from_none], obj.get("typeName"))
        name = from_union([from_str, from_none], obj.get("name"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        email = from_union([from_str, from_none], obj.get("email"))
        country_id = from_union([from_str, from_none], obj.get("countryId"))
        country = from_union([from_str, from_none], obj.get("country"))
        address1 = from_union([from_str, from_none], obj.get("address1"))
        address2 = from_union([from_str, from_none], obj.get("address2"))
        city = from_union([from_str, from_none], obj.get("city"))
        state_id = from_union([from_str, from_none], obj.get("stateId"))
        roles = from_union([lambda x: from_list(from_str, x), from_none], obj.get("roles"))
        is_public = from_union([from_bool, from_none], obj.get("isPublic"))
        has_logo = from_union([from_bool, from_none], obj.get("hasLogo"))
        is_good_standing = from_union([from_bool, from_none], obj.get("isGoodStanding"))
        is_prohibited = from_union([from_bool, from_none], obj.get("isProhibited"))
        is_questionable = from_union([from_bool, from_none], obj.get("isQuestionable"))
        is_attorney = from_union([from_bool, from_none], obj.get("isAttorney"))
        is_sponsor = from_union([from_bool, from_none], obj.get("isSponsor"))
        public = from_union([from_bool, from_none], obj.get("public"))
        return Auditor(zip, id, type, type_id, type_name, name, phone, email, country_id, country, address1, address2, city, state_id, roles, is_public, has_logo, is_good_standing, is_prohibited, is_questionable, is_attorney, is_sponsor, public)

    def to_dict(self) -> dict:
        result: dict = {}
        result["zip"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.zip)
        result["id"] = from_union([from_int, from_none], self.id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["typeId"] = from_union([from_int, from_none], self.type_id)
        result["typeName"] = from_union([from_str, from_none], self.type_name)
        result["name"] = from_union([from_str, from_none], self.name)
        result["phone"] = from_union([from_str, from_none], self.phone)
        result["email"] = from_union([from_str, from_none], self.email)
        result["countryId"] = from_union([from_str, from_none], self.country_id)
        result["country"] = from_union([from_str, from_none], self.country)
        result["address1"] = from_union([from_str, from_none], self.address1)
        result["address2"] = from_union([from_str, from_none], self.address2)
        result["city"] = from_union([from_str, from_none], self.city)
        result["stateId"] = from_union([from_str, from_none], self.state_id)
        result["roles"] = from_union([lambda x: from_list(from_str, x), from_none], self.roles)
        result["isPublic"] = from_union([from_bool, from_none], self.is_public)
        result["hasLogo"] = from_union([from_bool, from_none], self.has_logo)
        result["isGoodStanding"] = from_union([from_bool, from_none], self.is_good_standing)
        result["isProhibited"] = from_union([from_bool, from_none], self.is_prohibited)
        result["isQuestionable"] = from_union([from_bool, from_none], self.is_questionable)
        result["isAttorney"] = from_union([from_bool, from_none], self.is_attorney)
        result["isSponsor"] = from_union([from_bool, from_none], self.is_sponsor)
        result["public"] = from_union([from_bool, from_none], self.public)
        return result


@dataclass
class Officer:
    name: Optional[str] = None
    title: Optional[str] = None
    boards: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Officer':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        title = from_union([from_str, from_none], obj.get("title"))
        boards = from_union([from_str, from_none], obj.get("boards"))
        return Officer(name, title, boards)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["title"] = from_union([from_str, from_none], self.title)
        result["boards"] = from_union([from_str, from_none], self.boards)
        return result


@dataclass
class OtcAward:
    symbol: Optional[str] = None
    best50: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OtcAward':
        assert isinstance(obj, dict)
        symbol = from_union([from_str, from_none], obj.get("symbol"))
        best50 = from_union([from_bool, from_none], obj.get("best50"))
        return OtcAward(symbol, best50)

    def to_dict(self) -> dict:
        result: dict = {}
        result["symbol"] = from_union([from_str, from_none], self.symbol)
        result["best50"] = from_union([from_bool, from_none], self.best50)
        return result


@dataclass
class ProfileBadges:
    is_shell: Optional[bool] = None
    has_control_dispute: Optional[bool] = None
    is_penny_stock_exempt: Optional[bool] = None
    is_bankrupt: Optional[bool] = None
    unable_to_contact: Optional[bool] = None
    transfer_agent_verified: Optional[bool] = None
    is_caveat_emptor: Optional[bool] = None
    is_dark: Optional[bool] = None
    is_delinquent: Optional[bool] = None
    has_promotion: Optional[bool] = None
    is_shell_risk: Optional[bool] = None
    is_linked_to_prohibited_sp: Optional[bool] = None
    verified_profile: Optional[bool] = None
    verified_date: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProfileBadges':
        assert isinstance(obj, dict)
        is_shell = from_union([from_bool, from_none], obj.get("isShell"))
        has_control_dispute = from_union([from_bool, from_none], obj.get("hasControlDispute"))
        is_penny_stock_exempt = from_union([from_bool, from_none], obj.get("isPennyStockExempt"))
        is_bankrupt = from_union([from_bool, from_none], obj.get("isBankrupt"))
        unable_to_contact = from_union([from_bool, from_none], obj.get("unableToContact"))
        transfer_agent_verified = from_union([from_bool, from_none], obj.get("transferAgentVerified"))
        is_caveat_emptor = from_union([from_bool, from_none], obj.get("isCaveatEmptor"))
        is_dark = from_union([from_bool, from_none], obj.get("isDark"))
        is_delinquent = from_union([from_bool, from_none], obj.get("isDelinquent"))
        has_promotion = from_union([from_bool, from_none], obj.get("hasPromotion"))
        is_shell_risk = from_union([from_bool, from_none], obj.get("isShellRisk"))
        is_linked_to_prohibited_sp = from_union([from_bool, from_none], obj.get("isLinkedToProhibitedSP"))
        verified_profile = from_union([from_bool, from_none], obj.get("verifiedProfile"))
        verified_date = from_union([from_int, from_none], obj.get("verifiedDate"))
        return ProfileBadges(is_shell, has_control_dispute, is_penny_stock_exempt, is_bankrupt, unable_to_contact, transfer_agent_verified, is_caveat_emptor, is_dark, is_delinquent, has_promotion, is_shell_risk, is_linked_to_prohibited_sp, verified_profile, verified_date)

    def to_dict(self) -> dict:
        result: dict = {}
        result["isShell"] = from_union([from_bool, from_none], self.is_shell)
        result["hasControlDispute"] = from_union([from_bool, from_none], self.has_control_dispute)
        result["isPennyStockExempt"] = from_union([from_bool, from_none], self.is_penny_stock_exempt)
        result["isBankrupt"] = from_union([from_bool, from_none], self.is_bankrupt)
        result["unableToContact"] = from_union([from_bool, from_none], self.unable_to_contact)
        result["transferAgentVerified"] = from_union([from_bool, from_none], self.transfer_agent_verified)
        result["isCaveatEmptor"] = from_union([from_bool, from_none], self.is_caveat_emptor)
        result["isDark"] = from_union([from_bool, from_none], self.is_dark)
        result["isDelinquent"] = from_union([from_bool, from_none], self.is_delinquent)
        result["hasPromotion"] = from_union([from_bool, from_none], self.has_promotion)
        result["isShellRisk"] = from_union([from_bool, from_none], self.is_shell_risk)
        result["isLinkedToProhibitedSP"] = from_union([from_bool, from_none], self.is_linked_to_prohibited_sp)
        result["verifiedProfile"] = from_union([from_bool, from_none], self.verified_profile)
        result["verifiedDate"] = from_union([from_int, from_none], self.verified_date)
        return result


@dataclass
class Security:
    id: Optional[int] = None
    tier_id: Optional[int] = None
    symbol: Optional[str] = None
    cusip: Optional[str] = None
    comp_id: Optional[int] = None
    issue_name: Optional[str] = None
    class_name: Optional[str] = None
    primary_venue: Optional[str] = None
    category_id: Optional[int] = None
    category_name: Optional[str] = None
    is_bb: Optional[bool] = None
    is_pink_sheets: Optional[bool] = None
    is_no_info: Optional[bool] = None
    has_level2: Optional[bool] = None
    is_level2_entitled: Optional[bool] = None
    type_code: Optional[str] = None
    type_name: Optional[str] = None
    tier_name: Optional[str] = None
    tier_group_id: Optional[str] = None
    tier_code: Optional[str] = None
    tier_start_date: Optional[int] = None
    tier_display_name: Optional[str] = None
    ratio_adr: Optional[int] = None
    is_adr: Optional[bool] = None
    is_gdr: Optional[bool] = None
    is_test: Optional[bool] = None
    is_otc_qx: Optional[bool] = None
    is_sponsored: Optional[bool] = None
    is_piggy_backed: Optional[bool] = None
    is_caveat_emptor: Optional[bool] = None
    can_access_bb: Optional[bool] = None
    no_par: Optional[bool] = None
    par_value: Optional[float] = None
    outstanding_shares: Optional[int] = None
    outstanding_shares_as_of_date: Optional[int] = None
    authorized_shares: Optional[int] = None
    dtc_shares: Optional[int] = None
    restricted_shares: Optional[int] = None
    unrestricted_shares: Optional[int] = None    
    unlimited_authorized_shares: Optional[bool] = None
    authorized_shares_as_of_date: Optional[int] = None
    public_float: Optional[int] = None
    public_float_as_of_date: Optional[int] = None
    is_exchange_qualified: Optional[bool] = None
    short_interest: Optional[int] = None
    short_interest_change: Optional[int] = None
    short_interest_date: Optional[int] = None
    sig_fail_deliver: Optional[bool] = None
    num_of_record_shareholders: Optional[int] = None
    num_of_record_shareholders_date: Optional[int] = None
    transfer_agents: Optional[List[Auditor]] = None
    notes: Optional[List[str]] = None
    is_unsolicited: Optional[bool] = None
    show_trusted_logo_for_authorized_shares: Optional[bool] = None
    show_trusted_logo_for_outstanding_shares: Optional[bool] = None
    show_trusted_logo_for_restricted_shares: Optional[bool] = None
    show_trusted_logo_for_unrestricted_shares: Optional[bool] = None
    show_trusted_logo_for_dtc_shares: Optional[bool] = None
    current_capital_change: Optional[str] = None
    current_capital_change_pay_date: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Security':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        tier_id = from_union([from_int, from_none], obj.get("tierId"))
        symbol = from_union([from_str, from_none], obj.get("symbol"))
        cusip = from_union([from_str, from_none], obj.get("cusip"))
        comp_id = from_union([from_int, from_none], obj.get("compId"))
        issue_name = from_union([from_str, from_none], obj.get("issueName"))
        class_name = from_union([from_str, from_none], obj.get("className"))
        primary_venue = from_union([from_str, from_none], obj.get("primaryVenue"))
        category_id = from_union([from_int, from_none], obj.get("categoryId"))
        category_name = from_union([from_str, from_none], obj.get("categoryName"))
        is_bb = from_union([from_bool, from_none], obj.get("isBB"))
        is_pink_sheets = from_union([from_bool, from_none], obj.get("isPinkSheets"))
        is_no_info = from_union([from_bool, from_none], obj.get("isNoInfo"))
        has_level2 = from_union([from_bool, from_none], obj.get("hasLevel2"))
        is_level2_entitled = from_union([from_bool, from_none], obj.get("isLevel2Entitled"))
        type_code = from_union([from_str, from_none], obj.get("typeCode"))
        type_name = from_union([from_str, from_none], obj.get("typeName"))
        tier_name = from_union([from_str, from_none], obj.get("tierName"))
        tier_group_id = from_union([from_str, from_none], obj.get("tierGroupId"))
        tier_code = from_union([from_str, from_none], obj.get("tierCode"))
        tier_start_date = from_union([from_int, from_none], obj.get("tierStartDate"))
        tier_display_name = from_union([from_str, from_none], obj.get("tierDisplayName"))
        ratio_adr = 1 #from_union([from_int, from_none], obj.get("ratioAdr"))
        is_adr = from_union([from_bool, from_none], obj.get("isAdr"))
        is_gdr = from_union([from_bool, from_none], obj.get("isGdr"))
        is_test = from_union([from_bool, from_none], obj.get("isTest"))
        is_otc_qx = from_union([from_bool, from_none], obj.get("isOtcQX"))
        is_sponsored = from_union([from_bool, from_none], obj.get("isSponsored"))
        is_piggy_backed = from_union([from_bool, from_none], obj.get("isPiggyBacked"))
        is_caveat_emptor = from_union([from_bool, from_none], obj.get("isCaveatEmptor"))
        can_access_bb = from_union([from_bool, from_none], obj.get("canAccessBB"))
        no_par = from_union([from_bool, from_none], obj.get("noPar"))
        par_value = from_union([from_float, from_none], obj.get("parValue"))
        outstanding_shares = from_union([from_int, from_none], obj.get("outstandingShares"))
        outstanding_shares_as_of_date = from_union([from_int, from_none], obj.get("outstandingSharesAsOfDate"))
        authorized_shares = from_union([from_int, from_none], obj.get("authorizedShares"))
        dtc_shares = from_union([from_int, from_none], obj.get("dtcShares"))
        restricted_shares = from_union([from_int, from_none], obj.get("restrictedShares"))
        unrestricted_shares = from_union([from_int, from_none], obj.get("unrestrictedShares"))
        unlimited_authorized_shares = from_union([from_bool, from_none], obj.get("unlimitedAuthorizedShares"))
        authorized_shares_as_of_date = from_union([from_int, from_none], obj.get("authorizedSharesAsOfDate"))
        public_float = from_union([from_int, from_none], obj.get("publicFloat"))
        public_float_as_of_date = from_union([from_int, from_none], obj.get("publicFloatAsOfDate"))
        is_exchange_qualified = from_union([from_bool, from_none], obj.get("isExchangeQualified"))
        short_interest = from_union([from_int, from_none], obj.get("shortInterest"))
        short_interest_change = 0 #from_union([from_int, from_none], obj.get("shortInterestChange"))
        short_interest_date = from_union([from_int, from_none], obj.get("shortInterestDate"))
        sig_fail_deliver = from_union([from_bool, from_none], obj.get("sigFailDeliver"))
        num_of_record_shareholders = from_union([from_int, from_none], obj.get("numOfRecordShareholders"))
        num_of_record_shareholders_date = from_union([from_int, from_none], obj.get("numOfRecordShareholdersDate"))
        transfer_agents = "" # from_union([lambda x: from_list(Auditor.from_dict, x), from_none], obj.get("transferAgents"))
        notes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("notes"))
        is_unsolicited = from_union([from_bool, from_none], obj.get("isUnsolicited"))
        show_trusted_logo_for_authorized_shares = from_union([from_bool, from_none], obj.get("showTrustedLogoForAuthorizedShares"))
        show_trusted_logo_for_outstanding_shares = from_union([from_bool, from_none], obj.get("showTrustedLogoForOutstandingShares"))
        show_trusted_logo_for_restricted_shares = from_union([from_bool, from_none], obj.get("showTrustedLogoForRestrictedShares"))
        show_trusted_logo_for_unrestricted_shares = from_union([from_bool, from_none], obj.get("showTrustedLogoForUnrestrictedShares"))
        show_trusted_logo_for_dtc_shares = from_union([from_bool, from_none], obj.get("showTrustedLogoForDTCShares"))
        current_capital_change = from_union([from_str, from_none], obj.get("currentCapitalChange"))
        current_capital_change_pay_date = from_union([from_int, from_none], obj.get("currentCapitalChangePayDate"))
        return Security(id, tier_id, symbol, cusip, comp_id, issue_name, class_name, primary_venue, category_id, category_name, is_bb, is_pink_sheets, is_no_info, has_level2, is_level2_entitled, type_code, type_name, tier_name, tier_group_id, tier_code, tier_start_date, tier_display_name, ratio_adr, is_adr, is_gdr, is_test, is_otc_qx, is_sponsored, is_piggy_backed, is_caveat_emptor, can_access_bb, no_par, par_value, outstanding_shares, outstanding_shares_as_of_date, authorized_shares, dtc_shares, restricted_shares, unrestricted_shares, unlimited_authorized_shares, authorized_shares_as_of_date, public_float, public_float_as_of_date, is_exchange_qualified, short_interest, short_interest_change, short_interest_date, sig_fail_deliver, num_of_record_shareholders, num_of_record_shareholders_date, transfer_agents, notes, is_unsolicited, show_trusted_logo_for_authorized_shares, show_trusted_logo_for_outstanding_shares, show_trusted_logo_for_restricted_shares, show_trusted_logo_for_unrestricted_shares, show_trusted_logo_for_dtc_shares, current_capital_change, current_capital_change_pay_date)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["tierId"] = from_union([from_int, from_none], self.tier_id)
        result["symbol"] = from_union([from_str, from_none], self.symbol)
        result["cusip"] = from_union([from_str, from_none], self.cusip)
        result["compId"] = from_union([from_int, from_none], self.comp_id)
        result["issueName"] = from_union([from_str, from_none], self.issue_name)
        result["className"] = from_union([from_str, from_none], self.class_name)
        result["primaryVenue"] = from_union([from_str, from_none], self.primary_venue)
        result["categoryId"] = from_union([from_int, from_none], self.category_id)
        result["categoryName"] = from_union([from_str, from_none], self.category_name)
        result["isBB"] = from_union([from_bool, from_none], self.is_bb)
        result["isPinkSheets"] = from_union([from_bool, from_none], self.is_pink_sheets)
        result["isNoInfo"] = from_union([from_bool, from_none], self.is_no_info)
        result["hasLevel2"] = from_union([from_bool, from_none], self.has_level2)
        result["isLevel2Entitled"] = from_union([from_bool, from_none], self.is_level2_entitled)
        result["typeCode"] = from_union([from_str, from_none], self.type_code)
        result["typeName"] = from_union([from_str, from_none], self.type_name)
        result["tierName"] = from_union([from_str, from_none], self.tier_name)
        result["tierGroupId"] = from_union([from_str, from_none], self.tier_group_id)
        result["tierCode"] = from_union([from_str, from_none], self.tier_code)
        result["tierStartDate"] = from_union([from_int, from_none], self.tier_start_date)
        result["tierDisplayName"] = from_union([from_str, from_none], self.tier_display_name)
        result["ratioAdr"] = from_union([from_int, from_none], self.ratio_adr)
        result["isAdr"] = from_union([from_bool, from_none], self.is_adr)
        result["isGdr"] = from_union([from_bool, from_none], self.is_gdr)
        result["isTest"] = from_union([from_bool, from_none], self.is_test)
        result["isOtcQX"] = from_union([from_bool, from_none], self.is_otc_qx)
        result["isSponsored"] = from_union([from_bool, from_none], self.is_sponsored)
        result["isPiggyBacked"] = from_union([from_bool, from_none], self.is_piggy_backed)
        result["isCaveatEmptor"] = from_union([from_bool, from_none], self.is_caveat_emptor)
        result["canAccessBB"] = from_union([from_bool, from_none], self.can_access_bb)
        result["noPar"] = from_union([from_bool, from_none], self.no_par)
        result["parValue"] = from_union([to_float, from_none], self.par_value)
        result["outstandingShares"] = from_union([from_int, from_none], self.outstanding_shares)
        result["outstandingSharesAsOfDate"] = from_union([from_int, from_none], self.outstanding_shares_as_of_date)
        result["authorizedShares"] = from_union([from_int, from_none], self.authorized_shares)
        result["unlimitedAuthorizedShares"] = from_union([from_bool, from_none], self.unlimited_authorized_shares)
        result["authorizedSharesAsOfDate"] = from_union([from_int, from_none], self.authorized_shares_as_of_date)
        result["dtcShares"] = from_union([from_int, from_none], self.dtc_shares)
        result["restrictedShares"] = from_union([from_int, from_none], self.restricted_shares)
        result["unrestrictedShares"] = from_union([from_int, from_none], self.unrestricted_shares)
        result["publicFloat"] = from_union([from_int, from_none], self.public_float)
        result["publicFloatAsOfDate"] = from_union([from_int, from_none], self.public_float_as_of_date)
        result["isExchangeQualified"] = from_union([from_bool, from_none], self.is_exchange_qualified)
        result["shortInterest"] = from_union([from_int, from_none], self.short_interest)
        result["shortInterestChange"] = from_union([from_int, from_none], self.short_interest_change)
        result["shortInterestDate"] = from_union([from_int, from_none], self.short_interest_date)
        result["sigFailDeliver"] = from_union([from_bool, from_none], self.sig_fail_deliver)
        result["numOfRecordShareholders"] = from_union([from_int, from_none], self.num_of_record_shareholders)
        result["numOfRecordShareholdersDate"] = from_union([from_int, from_none], self.num_of_record_shareholders_date)
        result["transferAgents"] = "" #from_union([lambda x: from_list(lambda x: to_class(Auditor, x), x), from_none], self.transfer_agents)
        result["notes"] = from_union([lambda x: from_list(from_str, x), from_none], self.notes)
        result["isUnsolicited"] = from_union([from_bool, from_none], self.is_unsolicited)
        result["showTrustedLogoForAuthorizedShares"] = from_union([from_bool, from_none], self.show_trusted_logo_for_authorized_shares)
        result["showTrustedLogoForOutstandingShares"] = from_union([from_bool, from_none], self.show_trusted_logo_for_outstanding_shares)
        result["showTrustedLogoForRestrictedShares"] = from_union([from_bool, from_none], self.show_trusted_logo_for_restricted_shares)
        result["showTrustedLogoForUnrestrictedShares"] = from_union([from_bool, from_none], self.show_trusted_logo_for_unrestricted_shares)
        result["showTrustedLogoForDTCShares"] = from_union([from_bool, from_none], self.show_trusted_logo_for_dtc_shares)
        result["currentCapitalChange"] = from_union([from_str, from_none], self.current_capital_change)
        result["currentCapitalChangePayDate"] = from_union([from_int, from_none], self.current_capital_change_pay_date)
        return result


@dataclass
class Otc:
    year_of_incorporation: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country_id: Optional[str] = None
    country: Optional[str] = None
    address1: Optional[str] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    business_desc: Optional[str] = None
    state_of_incorporation: Optional[str] = None
    state_of_incorporation_name: Optional[str] = None
    country_of_incorporation: Optional[str] = None
    country_of_incorporation_name: Optional[str] = None
    premier_director_list: Optional[List[Any]] = None
    standard_director_list: Optional[List[Any]] = None
    officers: Optional[List[Officer]] = None
    fiscal_year_end: Optional[str] = None
    filing_cycle: Optional[str] = None
    edgar_filing_status: Optional[str] = None
    edgar_filing_status_id: Optional[str] = None
    reporting_standard: Optional[str] = None
    reporting_standard_min: Optional[str] = None
    is_dark: Optional[bool] = None
    deregistered: Optional[bool] = None
    deregistration_date: Optional[int] = None
    is12_g32_b: Optional[bool] = None
    cik: Optional[str] = None
    is_alternative_reporting: Optional[bool] = None
    is_bank_thrift: Optional[bool] = None
    is_non_bank_regulated: Optional[bool] = None
    is_international_reporting: Optional[bool] = None
    is_other_reporting: Optional[bool] = None
    audited_status_display: Optional[str] = None
    audit_status: Optional[str] = None
    audited: Optional[bool] = None
    email: Optional[str] = None
    number_of_record_shareholders: Optional[int] = None
    number_of_record_shareholders_date: Optional[int] = None
    primary_sic_code: Optional[str] = None
    auditors: Optional[List[Auditor]] = None
    investor_relation_firms: Optional[List[Any]] = None
    legal_counsels: Optional[List[Auditor]] = None
    investment_banks: Optional[List[Any]] = None
    notes: Optional[List[str]] = None
    securities: Optional[List[Security]] = None
    other_securities: Optional[List[Any]] = None
    estimated_market_cap: Optional[float] = None
    estimated_market_cap_as_of_date: Optional[int] = None
    blank_check: Optional[bool] = None
    blind_pool: Optional[bool] = None
    spac: Optional[bool] = None
    has_latest_filing: Optional[bool] = None
    latest_filing_type: Optional[str] = None
    latest_filing_date: Optional[int] = None
    latest_filing_url: Optional[str] = None
    tier_group: Optional[str] = None
    tier_code: Optional[str] = None
    tier_start_date: Optional[int] = None
    has_logo: Optional[bool] = None
    company_logo_url: Optional[str] = None
    is_caveat_emptor: Optional[bool] = None
    otc_award: Optional[OtcAward] = None
    index_statuses: Optional[List[Any]] = None
    profile_badges: Optional[ProfileBadges] = None
    unable_to_contact: Optional[bool] = None
    is_shell: Optional[bool] = None
    is_bankrupt: Optional[bool] = None
    is_profile_verified: Optional[bool] = None
    venue: Optional[str] = None
    is_unsolicited: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Otc':
        assert isinstance(obj, dict)
        year_of_incorporation = from_union([from_none, lambda x: int(from_str(x))], obj.get("yearOfIncorporation"))
        id = from_union([from_int, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        city = from_union([from_str, from_none], obj.get("city"))
        state = from_union([from_str, from_none], obj.get("state"))
        zip = from_union([from_str, from_none], obj.get("zip"))
        country_id = from_union([from_str, from_none], obj.get("countryId"))
        country = from_union([from_str, from_none], obj.get("country"))
        address1 = from_union([from_str, from_none], obj.get("address1"))
        website = from_union([from_str, from_none], obj.get("website"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        fax = from_union([from_str, from_none], obj.get("fax"))
        business_desc = from_union([from_str, from_none], obj.get("businessDesc"))
        state_of_incorporation = from_union([from_str, from_none], obj.get("stateOfIncorporation"))
        state_of_incorporation_name = from_union([from_str, from_none], obj.get("stateOfIncorporationName"))
        country_of_incorporation = from_union([from_str, from_none], obj.get("countryOfIncorporation"))
        country_of_incorporation_name = from_union([from_str, from_none], obj.get("countryOfIncorporationName"))
        premier_director_list = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("premierDirectorList"))
        standard_director_list = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("standardDirectorList"))
        officers = from_union([lambda x: from_list(Officer.from_dict, x), from_none], obj.get("officers"))
        fiscal_year_end = from_union([from_str, from_none], obj.get("fiscalYearEnd"))
        filing_cycle = from_union([from_str, from_none], obj.get("filingCycle"))
        edgar_filing_status = from_union([from_str, from_none], obj.get("edgarFilingStatus"))
        edgar_filing_status_id = from_union([from_str, from_none], obj.get("edgarFilingStatusId"))
        reporting_standard = from_union([from_str, from_none], obj.get("reportingStandard"))
        reporting_standard_min = from_union([from_str, from_none], obj.get("reportingStandardMin"))
        is_dark = from_union([from_bool, from_none], obj.get("isDark"))
        deregistered = from_union([from_bool, from_none], obj.get("deregistered"))
        deregistration_date = from_union([from_int, from_none], obj.get("deregistrationDate"))
        is12_g32_b = from_union([from_bool, from_none], obj.get("is12g32b"))
        cik = from_union([from_str, from_none], obj.get("cik"))
        is_alternative_reporting = from_union([from_bool, from_none], obj.get("isAlternativeReporting"))
        is_bank_thrift = from_union([from_bool, from_none], obj.get("isBankThrift"))
        is_non_bank_regulated = from_union([from_bool, from_none], obj.get("isNonBankRegulated"))
        is_international_reporting = from_union([from_bool, from_none], obj.get("isInternationalReporting"))
        is_other_reporting = from_union([from_bool, from_none], obj.get("isOtherReporting"))
        audited_status_display = from_union([from_str, from_none], obj.get("auditedStatusDisplay"))
        audit_status = from_union([from_str, from_none], obj.get("auditStatus"))
        audited = from_union([from_bool, from_none], obj.get("audited"))
        email = from_union([from_str, from_none], obj.get("email"))
        number_of_record_shareholders = from_union([from_int, from_none], obj.get("numberOfRecordShareholders"))
        number_of_record_shareholders_date = from_union([from_int, from_none], obj.get("numberOfRecordShareholdersDate"))
        primary_sic_code = from_union([from_str, from_none], obj.get("primarySicCode"))
        auditors = "" #from_union([lambda x: from_list(Auditor.from_dict, x), from_none], obj.get("auditors"))
        investor_relation_firms = "" # from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("investorRelationFirms"))
        legal_counsels = "" # from_union([lambda x: from_list(Auditor.from_dict, x), from_none], obj.get("legalCounsels"))
        investment_banks = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("investmentBanks"))
        notes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("notes"))
        securities = from_union([lambda x: from_list(Security.from_dict, x), from_none], obj.get("securities"))
        other_securities = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("otherSecurities"))
        estimated_market_cap = from_union([from_float, from_none], obj.get("estimatedMarketCap"))
        estimated_market_cap_as_of_date = from_union([from_int, from_none], obj.get("estimatedMarketCapAsOfDate"))
        blank_check = from_union([from_bool, from_none], obj.get("blankCheck"))
        blind_pool = from_union([from_bool, from_none], obj.get("blindPool"))
        spac = from_union([from_bool, from_none], obj.get("spac"))
        has_latest_filing = from_union([from_bool, from_none], obj.get("hasLatestFiling"))
        latest_filing_type = from_union([from_str, from_none], obj.get("latestFilingType"))
        latest_filing_date = from_union([from_int, from_none], obj.get("latestFilingDate"))
        latest_filing_url = from_union([from_str, from_none], obj.get("latestFilingUrl"))
        tier_group = from_union([from_str, from_none], obj.get("tierGroup"))
        tier_code = from_union([from_str, from_none], obj.get("tierCode"))
        tier_start_date = from_union([from_int, from_none], obj.get("tierStartDate"))
        has_logo = from_union([from_bool, from_none], obj.get("hasLogo"))
        company_logo_url = from_union([from_str, from_none], obj.get("companyLogoUrl"))
        is_caveat_emptor = from_union([from_bool, from_none], obj.get("isCaveatEmptor"))
        otc_award = from_union([OtcAward.from_dict, from_none], obj.get("otcAward"))
        index_statuses = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("indexStatuses"))
        profile_badges = from_union([ProfileBadges.from_dict, from_none], obj.get("profileBadges"))
        unable_to_contact = from_union([from_bool, from_none], obj.get("unableToContact"))
        is_shell = from_union([from_bool, from_none], obj.get("isShell"))
        is_bankrupt = from_union([from_bool, from_none], obj.get("isBankrupt"))
        is_profile_verified = from_union([from_bool, from_none], obj.get("isProfileVerified"))
        venue = from_union([from_str, from_none], obj.get("venue"))
        is_unsolicited = from_union([from_bool, from_none], obj.get("isUnsolicited"))
        return Otc(year_of_incorporation, id, name, city, state, zip, country_id, country, address1, website, phone, fax, business_desc, state_of_incorporation, state_of_incorporation_name, country_of_incorporation, country_of_incorporation_name, premier_director_list, standard_director_list, officers, fiscal_year_end, filing_cycle, edgar_filing_status, edgar_filing_status_id, reporting_standard, reporting_standard_min, is_dark, deregistered, deregistration_date, is12_g32_b, cik, is_alternative_reporting, is_bank_thrift, is_non_bank_regulated, is_international_reporting, is_other_reporting, audited_status_display, audit_status, audited, email, number_of_record_shareholders, number_of_record_shareholders_date, primary_sic_code, auditors, investor_relation_firms, legal_counsels, investment_banks, notes, securities, other_securities, estimated_market_cap, estimated_market_cap_as_of_date, blank_check, blind_pool, spac, has_latest_filing, latest_filing_type, latest_filing_date, latest_filing_url, tier_group, tier_code, tier_start_date, has_logo, company_logo_url, is_caveat_emptor, otc_award, index_statuses, profile_badges, unable_to_contact, is_shell, is_bankrupt, is_profile_verified, venue, is_unsolicited)

    def to_dict(self) -> dict:
        result: dict = {}
        result["yearOfIncorporation"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.year_of_incorporation)
        result["id"] = from_union([from_int, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["city"] = from_union([from_str, from_none], self.city)
        result["state"] = from_union([from_str, from_none], self.state)
        result["zip"] = from_union([from_str, from_none], self.zip)
        result["countryId"] = from_union([from_str, from_none], self.country_id)
        result["country"] = from_union([from_str, from_none], self.country)
        result["address1"] = from_union([from_str, from_none], self.address1)
        result["website"] = from_union([from_str, from_none], self.website)
        result["phone"] = from_union([from_str, from_none], self.phone)
        result["fax"] = from_union([from_str, from_none], self.fax)
        result["businessDesc"] = from_union([from_str, from_none], self.business_desc)
        result["stateOfIncorporation"] = from_union([from_str, from_none], self.state_of_incorporation)
        result["stateOfIncorporationName"] = from_union([from_str, from_none], self.state_of_incorporation_name)
        result["countryOfIncorporation"] = from_union([from_str, from_none], self.country_of_incorporation)
        result["countryOfIncorporationName"] = from_union([from_str, from_none], self.country_of_incorporation_name)
        result["premierDirectorList"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.premier_director_list)
        result["standardDirectorList"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.standard_director_list)
        result["officers"] = from_union([lambda x: from_list(lambda x: to_class(Officer, x), x), from_none], self.officers)
        result["fiscalYearEnd"] = from_union([from_str, from_none], self.fiscal_year_end)
        result["filingCycle"] = from_union([from_str, from_none], self.filing_cycle)
        result["edgarFilingStatus"] = from_union([from_str, from_none], self.edgar_filing_status)
        result["edgarFilingStatusId"] = from_union([from_str, from_none], self.edgar_filing_status_id)
        result["reportingStandard"] = from_union([from_str, from_none], self.reporting_standard)
        result["reportingStandardMin"] = from_union([from_str, from_none], self.reporting_standard_min)
        result["isDark"] = from_union([from_bool, from_none], self.is_dark)
        result["deregistered"] = from_union([from_bool, from_none], self.deregistered)
        result["deregistrationDate"] = from_union([from_int, from_none], self.deregistration_date)
        result["is12g32b"] = from_union([from_bool, from_none], self.is12_g32_b)
        result["cik"] = from_union([from_str, from_none], self.cik)
        result["isAlternativeReporting"] = from_union([from_bool, from_none], self.is_alternative_reporting)
        result["isBankThrift"] = from_union([from_bool, from_none], self.is_bank_thrift)
        result["isNonBankRegulated"] = from_union([from_bool, from_none], self.is_non_bank_regulated)
        result["isInternationalReporting"] = from_union([from_bool, from_none], self.is_international_reporting)
        result["isOtherReporting"] = from_union([from_bool, from_none], self.is_other_reporting)
        result["auditedStatusDisplay"] = from_union([from_str, from_none], self.audited_status_display)
        result["auditStatus"] = from_union([from_str, from_none], self.audit_status)
        result["audited"] = from_union([from_bool, from_none], self.audited)
        result["email"] = from_union([from_str, from_none], self.email)
        result["numberOfRecordShareholders"] = from_union([from_int, from_none], self.number_of_record_shareholders)
        result["numberOfRecordShareholdersDate"] = from_union([from_int, from_none], self.number_of_record_shareholders_date)
        result["primarySicCode"] = from_union([from_str, from_none], self.primary_sic_code)
        result["auditors"] = "" #from_union([lambda x: from_list(lambda x: to_class(Auditor, x), x), from_none], self.auditors)
        result["investorRelationFirms"] = "" #from_union([lambda x: from_list(lambda x: x, x), from_none], self.investor_relation_firms)
        result["legalCounsels"] = "" #from_union([lambda x: from_list(lambda x: to_class(Auditor, x), x), from_none], self.legal_counsels)
        result["investmentBanks"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.investment_banks)
        result["notes"] = from_union([lambda x: from_list(from_str, x), from_none], self.notes)
        result["securities"] = from_union([lambda x: from_list(lambda x: to_class(Security, x), x), from_none], self.securities)
        result["securities"] = result["securities"][0] #overwrite using the top level
        result["otherSecurities"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.other_securities)
        result["estimatedMarketCap"] = from_union([to_float, from_none], self.estimated_market_cap)
        result["estimatedMarketCapAsOfDate"] = from_union([from_int, from_none], self.estimated_market_cap_as_of_date)
        result["blankCheck"] = from_union([from_bool, from_none], self.blank_check)
        result["blindPool"] = from_union([from_bool, from_none], self.blind_pool)
        result["spac"] = from_union([from_bool, from_none], self.spac)
        result["hasLatestFiling"] = from_union([from_bool, from_none], self.has_latest_filing)
        result["latestFilingType"] = from_union([from_str, from_none], self.latest_filing_type)
        result["latestFilingDate"] = from_union([from_int, from_none], self.latest_filing_date)
        result["latestFilingUrl"] = from_union([from_str, from_none], self.latest_filing_url)
        result["tierGroup"] = from_union([from_str, from_none], self.tier_group)
        result["tierCode"] = from_union([from_str, from_none], self.tier_code)
        result["tierStartDate"] = from_union([from_int, from_none], self.tier_start_date)
        result["hasLogo"] = from_union([from_bool, from_none], self.has_logo)
        result["companyLogoUrl"] = from_union([from_str, from_none], self.company_logo_url)
        result["isCaveatEmptor"] = from_union([from_bool, from_none], self.is_caveat_emptor)
        result["otcAward"] = from_union([lambda x: to_class(OtcAward, x), from_none], self.otc_award)
        result["indexStatuses"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.index_statuses)
        result["profileBadges"] = from_union([lambda x: to_class(ProfileBadges, x), from_none], self.profile_badges)
        result["unableToContact"] = from_union([from_bool, from_none], self.unable_to_contact)
        result["isShell"] = from_union([from_bool, from_none], self.is_shell)
        result["isBankrupt"] = from_union([from_bool, from_none], self.is_bankrupt)
        result["isProfileVerified"] = from_union([from_bool, from_none], self.is_profile_verified)
        result["venue"] = from_union([from_str, from_none], self.venue)
        result["isUnsolicited"] = from_union([from_bool, from_none], self.is_unsolicited)
        return result


def otc_from_dict(s: Any) -> Otc:
    return Otc.from_dict(s)


def otc_to_dict(x: Otc) -> Any:
    return to_class(Otc, x)
