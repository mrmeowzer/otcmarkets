# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Stock:
    security_id: Optional[int] = None
    report_date: Optional[str] = None
    symbol: Optional[str] = None
    security_name: Optional[str] = None
    market: Optional[str] = None
    market_id: Optional[int] = None
    security_type: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    forex_country: Optional[str] = None
    caveat_emptor: Optional[bool] = None
    industry_id: Optional[int] = None
    industry: Optional[str] = None
    volume: Optional[int] = None
    volume_change: Optional[float] = None
    dividend_yield: Optional[float] = None
    dividend_payer: Optional[bool] = None
    morning_star_rating: Optional[int] = None
    penny: Optional[bool] = None
    price: Optional[float] = None
    short_interest: Optional[int] = None
    short_interest_percent: Optional[float] = None
    short_interest_ratio: Optional[float] = None
    is_bank: Optional[str] = None
    pct1_day: Optional[float] = None
    pct5_day: Optional[float] = None
    pct4_weeks: Optional[float] = None
    pct13_weeks: Optional[float] = None
    pct52_weeks: Optional[float] = None
    perf_qx_comp4_weeks: Optional[float] = None
    perf_qx_comp13_weeks: Optional[float] = None
    perf_qx_comp52_weeks: Optional[float] = None
    perf_qx_billion4_weeks: Optional[float] = None
    perf_qx_billion13_weeks: Optional[float] = None
    perf_qx_billion52_weeks: Optional[float] = None
    perf_qx_banks4_weeks: Optional[float] = None
    perf_qx_banks13_weeks: Optional[float] = None
    perf_qx_banks52_weeks: Optional[float] = None
    perf_qx_intl4_weeks: Optional[float] = None
    perf_qx_intl13_weeks: Optional[float] = None
    perf_qx_intl52_weeks: Optional[float] = None
    perf_qx_us4_weeks: Optional[float] = None
    perf_qx_us13_weeks: Optional[float] = None
    perf_qx_us52_weeks: Optional[float] = None
    perf_qb4_weeks: Optional[float] = None
    perf_qb13_weeks: Optional[float] = None
    perf_qb52_weeks: Optional[float] = None
    perf_sp4_weeks: Optional[float] = None
    perf_sp13_weeks: Optional[float] = None
    perf_sp52_weeks: Optional[float] = None
    perf_qx_div4_weeks: Optional[float] = None
    perf_qx_div13_weeks: Optional[float] = None
    perf_qx_div52_weeks: Optional[float] = None
    perf_qx_can4_weeks: Optional[float] = None
    perf_qx_can13_weeks: Optional[float] = None
    perf_qx_can52_weeks: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Stock':
        assert isinstance(obj, dict)
        security_id = from_union([from_int, from_none], obj.get("securityId"))
        report_date = from_union([from_str, from_none], obj.get("reportDate"))
        symbol = from_union([from_str, from_none], obj.get("symbol"))
        security_name = from_union([from_str, from_none], obj.get("securityName"))
        market = from_union([from_str, from_none], obj.get("market"))
        market_id = from_union([from_int, from_none], obj.get("marketId"))
        security_type = from_union([from_str, from_none], obj.get("securityType"))
        country = from_union([from_str, from_none], obj.get("country"))
        state = from_union([from_str, from_none], obj.get("state"))
        forex_country = from_union([from_str, from_none], obj.get("forexCountry"))
        caveat_emptor = from_union([from_bool, from_none], obj.get("caveatEmptor"))
        industry_id = from_union([from_int, from_none], obj.get("industryId"))
        industry = from_union([from_str, from_none], obj.get("industry"))
        volume = from_union([from_int, from_none], obj.get("volume"))
        volume_change = from_union([from_float, from_none], obj.get("volumeChange"))
        dividend_yield = from_union([from_float, from_none], obj.get("dividendYield"))
        dividend_payer = from_union([from_bool, from_none], obj.get("dividendPayer"))
        morning_star_rating = from_union([from_int, from_none], obj.get("morningStarRating"))
        penny = from_union([from_bool, from_none], obj.get("penny"))
        price = from_union([from_float, from_none], obj.get("price"))
        short_interest = from_union([from_int, from_none], obj.get("shortInterest"))
        short_interest_percent = from_union([from_float, from_none], obj.get("shortInterestPercent"))
        short_interest_ratio = from_union([from_float, from_none], obj.get("shortInterestRatio"))
        is_bank = from_union([from_str, from_none], obj.get("isBank"))
        pct1_day = from_union([from_float, from_none], obj.get("pct1Day"))
        pct5_day = from_union([from_float, from_none], obj.get("pct5Day"))
        pct4_weeks = from_union([from_float, from_none], obj.get("pct4Weeks"))
        pct13_weeks = from_union([from_float, from_none], obj.get("pct13Weeks"))
        pct52_weeks = from_union([from_float, from_none], obj.get("pct52Weeks"))
        perf_qx_comp4_weeks = from_union([from_float, from_none], obj.get("perfQxComp4Weeks"))
        perf_qx_comp13_weeks = from_union([from_float, from_none], obj.get("perfQxComp13Weeks"))
        perf_qx_comp52_weeks = from_union([from_float, from_none], obj.get("perfQxComp52Weeks"))
        perf_qx_billion4_weeks = from_union([from_float, from_none], obj.get("perfQxBillion4Weeks"))
        perf_qx_billion13_weeks = from_union([from_float, from_none], obj.get("perfQxBillion13Weeks"))
        perf_qx_billion52_weeks = from_union([from_float, from_none], obj.get("perfQxBillion52Weeks"))
        perf_qx_banks4_weeks = from_union([from_float, from_none], obj.get("perfQxBanks4Weeks"))
        perf_qx_banks13_weeks = from_union([from_float, from_none], obj.get("perfQxBanks13Weeks"))
        perf_qx_banks52_weeks = from_union([from_float, from_none], obj.get("perfQxBanks52Weeks"))
        perf_qx_intl4_weeks = from_union([from_float, from_none], obj.get("perfQxIntl4Weeks"))
        perf_qx_intl13_weeks = from_union([from_float, from_none], obj.get("perfQxIntl13Weeks"))
        perf_qx_intl52_weeks = from_union([from_float, from_none], obj.get("perfQxIntl52Weeks"))
        perf_qx_us4_weeks = from_union([from_float, from_none], obj.get("perfQxUs4Weeks"))
        perf_qx_us13_weeks = from_union([from_float, from_none], obj.get("perfQxUs13Weeks"))
        perf_qx_us52_weeks = from_union([from_float, from_none], obj.get("perfQxUs52Weeks"))
        perf_qb4_weeks = from_union([from_float, from_none], obj.get("perfQb4Weeks"))
        perf_qb13_weeks = from_union([from_float, from_none], obj.get("perfQb13Weeks"))
        perf_qb52_weeks = from_union([from_float, from_none], obj.get("perfQb52Weeks"))
        perf_sp4_weeks = from_union([from_float, from_none], obj.get("perfSp4Weeks"))
        perf_sp13_weeks = from_union([from_float, from_none], obj.get("perfSp13Weeks"))
        perf_sp52_weeks = from_union([from_float, from_none], obj.get("perfSp52Weeks"))
        perf_qx_div4_weeks = from_union([from_float, from_none], obj.get("perfQxDiv4Weeks"))
        perf_qx_div13_weeks = from_union([from_float, from_none], obj.get("perfQxDiv13Weeks"))
        perf_qx_div52_weeks = from_union([from_float, from_none], obj.get("perfQxDiv52Weeks"))
        perf_qx_can4_weeks = from_union([from_float, from_none], obj.get("perfQxCan4Weeks"))
        perf_qx_can13_weeks = from_union([from_float, from_none], obj.get("perfQxCan13Weeks"))
        perf_qx_can52_weeks = from_union([from_float, from_none], obj.get("perfQxCan52Weeks"))
        return Stock(security_id, report_date, symbol, security_name, market, market_id, security_type, country, state, forex_country, caveat_emptor, industry_id, industry, volume, volume_change, dividend_yield, dividend_payer, morning_star_rating, penny, price, short_interest, short_interest_percent, short_interest_ratio, is_bank, pct1_day, pct5_day, pct4_weeks, pct13_weeks, pct52_weeks, perf_qx_comp4_weeks, perf_qx_comp13_weeks, perf_qx_comp52_weeks, perf_qx_billion4_weeks, perf_qx_billion13_weeks, perf_qx_billion52_weeks, perf_qx_banks4_weeks, perf_qx_banks13_weeks, perf_qx_banks52_weeks, perf_qx_intl4_weeks, perf_qx_intl13_weeks, perf_qx_intl52_weeks, perf_qx_us4_weeks, perf_qx_us13_weeks, perf_qx_us52_weeks, perf_qb4_weeks, perf_qb13_weeks, perf_qb52_weeks, perf_sp4_weeks, perf_sp13_weeks, perf_sp52_weeks, perf_qx_div4_weeks, perf_qx_div13_weeks, perf_qx_div52_weeks, perf_qx_can4_weeks, perf_qx_can13_weeks, perf_qx_can52_weeks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["securityId"] = from_union([from_int, from_none], self.security_id)
        result["reportDate"] = from_union([from_str, from_none], self.report_date)
        result["symbol"] = from_union([from_str, from_none], self.symbol)
        result["securityName"] = from_union([from_str, from_none], self.security_name)
        result["market"] = from_union([from_str, from_none], self.market)
        result["marketId"] = from_union([from_int, from_none], self.market_id)
        result["securityType"] = from_union([from_str, from_none], self.security_type)
        result["country"] = from_union([from_str, from_none], self.country)
        result["state"] = from_union([from_str, from_none], self.state)
        result["forexCountry"] = from_union([from_str, from_none], self.forex_country)
        result["caveatEmptor"] = from_union([from_bool, from_none], self.caveat_emptor)
        result["industryId"] = from_union([from_int, from_none], self.industry_id)
        result["industry"] = from_union([from_str, from_none], self.industry)
        result["volume"] = from_union([from_int, from_none], self.volume)
        result["volumeChange"] = from_union([to_float, from_none], self.volume_change)
        result["dividendYield"] = from_union([to_float, from_none], self.dividend_yield)
        result["dividendPayer"] = from_union([from_bool, from_none], self.dividend_payer)
        result["morningStarRating"] = from_union([from_int, from_none], self.morning_star_rating)
        result["penny"] = from_union([from_bool, from_none], self.penny)
        result["price"] = from_union([to_float, from_none], self.price)
        result["shortInterest"] = from_union([from_int, from_none], self.short_interest)
        result["shortInterestPercent"] = from_union([to_float, from_none], self.short_interest_percent)
        result["shortInterestRatio"] = from_union([to_float, from_none], self.short_interest_ratio)
        result["isBank"] = from_union([from_str, from_none], self.is_bank)
        result["pct1Day"] = from_union([to_float, from_none], self.pct1_day)
        result["pct5Day"] = from_union([to_float, from_none], self.pct5_day)
        result["pct4Weeks"] = from_union([to_float, from_none], self.pct4_weeks)
        result["pct13Weeks"] = from_union([to_float, from_none], self.pct13_weeks)
        result["pct52Weeks"] = from_union([to_float, from_none], self.pct52_weeks)
        result["perfQxComp4Weeks"] = from_union([to_float, from_none], self.perf_qx_comp4_weeks)
        result["perfQxComp13Weeks"] = from_union([to_float, from_none], self.perf_qx_comp13_weeks)
        result["perfQxComp52Weeks"] = from_union([to_float, from_none], self.perf_qx_comp52_weeks)
        result["perfQxBillion4Weeks"] = from_union([to_float, from_none], self.perf_qx_billion4_weeks)
        result["perfQxBillion13Weeks"] = from_union([to_float, from_none], self.perf_qx_billion13_weeks)
        result["perfQxBillion52Weeks"] = from_union([to_float, from_none], self.perf_qx_billion52_weeks)
        result["perfQxBanks4Weeks"] = from_union([to_float, from_none], self.perf_qx_banks4_weeks)
        result["perfQxBanks13Weeks"] = from_union([to_float, from_none], self.perf_qx_banks13_weeks)
        result["perfQxBanks52Weeks"] = from_union([to_float, from_none], self.perf_qx_banks52_weeks)
        result["perfQxIntl4Weeks"] = from_union([to_float, from_none], self.perf_qx_intl4_weeks)
        result["perfQxIntl13Weeks"] = from_union([to_float, from_none], self.perf_qx_intl13_weeks)
        result["perfQxIntl52Weeks"] = from_union([to_float, from_none], self.perf_qx_intl52_weeks)
        result["perfQxUs4Weeks"] = from_union([to_float, from_none], self.perf_qx_us4_weeks)
        result["perfQxUs13Weeks"] = from_union([to_float, from_none], self.perf_qx_us13_weeks)
        result["perfQxUs52Weeks"] = from_union([to_float, from_none], self.perf_qx_us52_weeks)
        result["perfQb4Weeks"] = from_union([to_float, from_none], self.perf_qb4_weeks)
        result["perfQb13Weeks"] = from_union([to_float, from_none], self.perf_qb13_weeks)
        result["perfQb52Weeks"] = from_union([to_float, from_none], self.perf_qb52_weeks)
        result["perfSp4Weeks"] = from_union([to_float, from_none], self.perf_sp4_weeks)
        result["perfSp13Weeks"] = from_union([to_float, from_none], self.perf_sp13_weeks)
        result["perfSp52Weeks"] = from_union([to_float, from_none], self.perf_sp52_weeks)
        result["perfQxDiv4Weeks"] = from_union([to_float, from_none], self.perf_qx_div4_weeks)
        result["perfQxDiv13Weeks"] = from_union([to_float, from_none], self.perf_qx_div13_weeks)
        result["perfQxDiv52Weeks"] = from_union([to_float, from_none], self.perf_qx_div52_weeks)
        result["perfQxCan4Weeks"] = from_union([to_float, from_none], self.perf_qx_can4_weeks)
        result["perfQxCan13Weeks"] = from_union([to_float, from_none], self.perf_qx_can13_weeks)
        result["perfQxCan52Weeks"] = from_union([to_float, from_none], self.perf_qx_can52_weeks)
        return result


@dataclass
class Welcome:
    count: Optional[int] = None
    pages: Optional[int] = None
    stocks: Optional[List[Stock]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Welcome':
        assert isinstance(obj, dict)
        count = from_union([from_int, from_none], obj.get("count"))
        pages = from_union([from_int, from_none], obj.get("pages"))
        stocks = from_union([lambda x: from_list(Stock.from_dict, x), from_none], obj.get("stocks"))
        return Welcome(count, pages, stocks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["count"] = from_union([from_int, from_none], self.count)
        result["pages"] = from_union([from_int, from_none], self.pages)
        result["stocks"] = from_union([lambda x: from_list(lambda x: to_class(Stock, x), x), from_none], self.stocks)
        return result


def welcome_from_dict(s: Any) -> Welcome:
    return Welcome.from_dict(s)


def welcome_to_dict(x: Welcome) -> Any:
    return to_class(Welcome, x)
