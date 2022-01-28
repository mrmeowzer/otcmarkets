# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = otccurrent_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Otccurrent:
    tick_code: Optional[int] = None
    exchange_code: Optional[int] = None
    is_otc: Optional[bool] = None
    symbol: Optional[str] = None
    security_id: Optional[int] = None
    last_sale: Optional[float] = None
    change: Optional[float] = None
    percent_change: Optional[float] = None
    tick_name: Optional[str] = None
    volume: Optional[int] = None
    volume_formatted: Optional[str] = None
    last_trade_time: Optional[int] = None
    quote_time: Optional[int] = None
    quote_date_time: Optional[int] = None
    inside_time: Optional[int] = None
    bid_price: Optional[float] = None
    bid_size: Optional[int] = None
    ask_price: Optional[float] = None
    ask_size: Optional[int] = None
    daily_high: Optional[float] = None
    daily_low: Optional[float] = None
    opening_price: Optional[float] = None
    annual_high: Optional[float] = None
    annual_low: Optional[float] = None
    eps: Optional[float] = None
    previous_close: Optional[float] = None
    beta_coefficient: Optional[float] = None
    exchange_name: Optional[str] = None
    delay: Optional[int] = None
    is_adr: Optional[bool] = None
    realtime: Optional[bool] = None
    pink_link_realtime: Optional[bool] = None
    thirty_days_avg_vol: Optional[float] = None
    show_realtime_ad: Optional[bool] = None
    market_cap: Optional[int] = None
    shares_outstanding: Optional[int] = None
    adr: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Otccurrent':
        assert isinstance(obj, dict)
        tick_code = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("tickCode"))
        exchange_code = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("exchangeCode"))
        is_otc = from_union([from_bool, from_none], obj.get("isOtc"))
        symbol = from_union([from_str, from_none], obj.get("symbol"))
        security_id = from_union([from_int, from_none], obj.get("securityId"))
        last_sale = from_union([from_float, from_none], obj.get("lastSale"))
        change = from_union([from_float, from_none], obj.get("change"))
        percent_change = from_union(
            [from_float, from_none], obj.get("percentChange"))
        tick_name = from_union([from_str, from_none], obj.get("tickName"))
        volume = from_union([from_int, from_none], obj.get("volume"))
        volume_formatted = from_union(
            [from_str, from_none], obj.get("volumeFormatted"))
        last_trade_time = from_union(
            [from_int, from_none], obj.get("lastTradeTime"))
        quote_time = from_union([from_int, from_none], obj.get("quoteTime"))
        quote_date_time = from_union(
            [from_int, from_none], obj.get("quoteDateTime"))
        inside_time = from_union([from_int, from_none], obj.get("insideTime"))
        bid_price = from_union([from_float, from_none], obj.get("bidPrice"))
        bid_size = from_union([from_int, from_none], obj.get("bidSize"))
        ask_price = from_union([from_float, from_none], obj.get("askPrice"))
        ask_size = from_union([from_int, from_none], obj.get("askSize"))
        daily_high = from_union([from_float, from_none], obj.get("dailyHigh"))
        daily_low = from_union([from_float, from_none], obj.get("dailyLow"))
        opening_price = from_union(
            [from_float, from_none], obj.get("openingPrice"))
        annual_high = from_union(
            [from_float, from_none], obj.get("annualHigh"))
        annual_low = from_union([from_float, from_none], obj.get("annualLow"))
        eps = from_union([from_float, from_none], obj.get("eps"))
        previous_close = from_union(
            [from_float, from_none], obj.get("previousClose"))
        beta_coefficient = from_union(
            [from_float, from_none], obj.get("betaCoefficient"))
        exchange_name = from_union(
            [from_str, from_none], obj.get("exchangeName"))
        delay = from_union([from_int, from_none], obj.get("delay"))
        is_adr = from_union([from_bool, from_none], obj.get("isADR"))
        realtime = from_union([from_bool, from_none], obj.get("realtime"))
        pink_link_realtime = from_union(
            [from_bool, from_none], obj.get("pinkLinkRealtime"))
        thirty_days_avg_vol = from_union(
            [from_float, from_none], obj.get("thirtyDaysAvgVol"))
        show_realtime_ad = from_union(
            [from_bool, from_none], obj.get("showRealtimeAd"))
        market_cap = from_union([from_int, from_none], obj.get("marketCap"))
        shares_outstanding = from_union(
            [from_int, from_none], obj.get("sharesOutstanding"))
        adr = from_union([from_bool, from_none], obj.get("adr"))
        return Otccurrent(tick_code, exchange_code, is_otc, symbol, security_id, last_sale, change, percent_change, tick_name, volume, volume_formatted, last_trade_time, quote_time, quote_date_time, inside_time, bid_price, bid_size, ask_price, ask_size, daily_high, daily_low, opening_price, annual_high, annual_low, eps, previous_close, beta_coefficient, exchange_name, delay, is_adr, realtime, pink_link_realtime, thirty_days_avg_vol, show_realtime_ad, market_cap, shares_outstanding, adr)

    def to_dict(self) -> dict:
        result: dict = {}
        result["tickCode"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(
            x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.tick_code)
        result["exchangeCode"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(
            x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.exchange_code)
        result["isOtc"] = from_union([from_bool, from_none], self.is_otc)
        result["symbol"] = from_union([from_str, from_none], self.symbol)
        result["securityId"] = from_union(
            [from_int, from_none], self.security_id)
        result["lastSale"] = from_union([to_float, from_none], self.last_sale)
        result["change"] = from_union([to_float, from_none], self.change)
        result["percentChange"] = from_union(
            [to_float, from_none], self.percent_change)
        result["tickName"] = from_union([from_str, from_none], self.tick_name)
        result["volume"] = from_union([from_int, from_none], self.volume)
        result["volumeFormatted"] = from_union(
            [from_str, from_none], self.volume_formatted)
        result["lastTradeTime"] = from_union(
            [from_int, from_none], self.last_trade_time)
        result["quoteTime"] = from_union(
            [from_int, from_none], self.quote_time)
        result["quoteDateTime"] = from_union(
            [from_int, from_none], self.quote_date_time)
        result["insideTime"] = from_union(
            [from_int, from_none], self.inside_time)
        result["bidPrice"] = from_union([to_float, from_none], self.bid_price)
        result["bidSize"] = from_union([from_int, from_none], self.bid_size)
        result["askPrice"] = from_union([to_float, from_none], self.ask_price)
        result["askSize"] = from_union([from_int, from_none], self.ask_size)
        result["dailyHigh"] = from_union(
            [to_float, from_none], self.daily_high)
        result["dailyLow"] = from_union([to_float, from_none], self.daily_low)
        result["openingPrice"] = from_union(
            [to_float, from_none], self.opening_price)
        result["annualHigh"] = from_union(
            [to_float, from_none], self.annual_high)
        result["annualLow"] = from_union(
            [to_float, from_none], self.annual_low)
        result["eps"] = from_union([to_float, from_none], self.eps)
        result["previousClose"] = from_union(
            [to_float, from_none], self.previous_close)
        result["betaCoefficient"] = from_union(
            [to_float, from_none], self.beta_coefficient)
        result["exchangeName"] = from_union(
            [from_str, from_none], self.exchange_name)
        result["delay"] = from_union([from_int, from_none], self.delay)
        result["isADR"] = from_union([from_bool, from_none], self.is_adr)
        result["realtime"] = from_union([from_bool, from_none], self.realtime)
        result["pinkLinkRealtime"] = from_union(
            [from_bool, from_none], self.pink_link_realtime)
        result["thirtyDaysAvgVol"] = from_union(
            [to_float, from_none], self.thirty_days_avg_vol)
        result["showRealtimeAd"] = from_union(
            [from_bool, from_none], self.show_realtime_ad)
        result["marketCap"] = from_union(
            [from_int, from_none], self.market_cap)
        result["sharesOutstanding"] = from_union(
            [from_int, from_none], self.shares_outstanding)
        result["adr"] = from_union([from_bool, from_none], self.adr)
        return result


def otccurrent_from_dict(s: Any) -> Otccurrent:
    return Otccurrent.from_dict(s)


def otccurrent_to_dict(x: Otccurrent) -> Any:
    return to_class(Otccurrent, x)
