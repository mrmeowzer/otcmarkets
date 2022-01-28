# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = otcprofile_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Otcprofile:
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
    has_two_ind_dir: Optional[bool] = None
    is_hot_sector: Optional[bool] = None
    symbol: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Otcprofile':
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
        has_two_ind_dir = from_union([from_bool, from_none], obj.get("hasTwoIndDir"))
        is_hot_sector = from_union([from_bool, from_none], obj.get("isHotSector"))
        symbol = from_union([from_str, from_none], obj.get("symbol"))
        return Otcprofile(is_shell, has_control_dispute, is_penny_stock_exempt, is_bankrupt, unable_to_contact, transfer_agent_verified, is_caveat_emptor, is_dark, is_delinquent, has_promotion, is_shell_risk, is_linked_to_prohibited_sp, verified_profile, verified_date, has_two_ind_dir, is_hot_sector, symbol)

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
        result["hasTwoIndDir"] = from_union([from_bool, from_none], self.has_two_ind_dir)
        result["isHotSector"] = from_union([from_bool, from_none], self.is_hot_sector)
        result["symbol"] = from_union([from_str, from_none], self.symbol)
        return result


def otcprofile_from_dict(s: Any) -> Otcprofile:
    return Otcprofile.from_dict(s)


def otcprofile_to_dict(x: Otcprofile) -> Any:
    return to_class(Otcprofile, x)
