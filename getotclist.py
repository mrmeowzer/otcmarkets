import otc
import otccurrent
import otcprofile
import json
import time
import random
import requests
import concurrent.futures
from datetime import datetime
from crud import session_scope
from models import Stock

MAX_THREADS = 2
MAX_NUM_ATTEMPTS = 50
OTCMARKETS_FULL_URL = "https://backend.otcmarkets.com/otcapi/company/profile/full/"
OTCMARKETS_INSIDE_URL = "https://backend.otcmarkets.com/otcapi/stock/trade/inside/"
OTCMARKETS_PROFILE_BADGE_URL = "https://backend.otcmarkets.com/otcapi/company/profile/"
OTCMARKETS_JSON = "https://www.otcmarkets.com/research/stock-screener/api?pageSize=50000&priceMax=.01&country=USA" #&ce=false&market=20,21,22,30,40"


def get_json():
    data = requests.get(OTCMARKETS_JSON).json()

    ticker_list = [x for x in json.loads(
        data)['stocks'] if len(x['symbol']) == 4]

    return ticker_list


def otc_response(url, ticker, otc_type):
    req = url
    result = {}
    message = ""
    try:
        for attempt in range(1, MAX_NUM_ATTEMPTS+1):
            response = requests.get(req)

            if response.status_code == 200:
                result = response.json()
                message = f"{ticker} found Type: {otc_type}"
                break
            elif response.status_code == 429:  # Too many requests
                # Wait between 30-60 seconds
                time.sleep(random.randint(30, 60))
                continue
            else:
                message = f"{ticker} not found ... Code: {response.status_code}"
                break
    except:
        pass

    if attempt >= MAX_NUM_ATTEMPTS:
        message = f"{ticker} unable to retrieve"  

    return message, result, ticker, otc_type


def prepare_data(otc_full_list, otc_inside_list, otc_profile_list):
    existing_set = get_existing(map(lambda x: x.symbol, otc_inside_list))

    insert_list = []
    update_list = []

    for stock in otc_inside_list:
        try:
            # Get stonk data from the "full" list
            full = [
                x for x in otc_full_list if x.securities[0].symbol == stock.symbol]
            
            # Get profile data from the "profile" list
            profile = [
                x for x in otc_profile_list if x.symbol == stock.symbol]

            if len(full) > 0:
                otc_data = full[0]
                security_data = otc_data.securities[0]
                profile_data = profile[0]

                # Get the id if exists in the DB
                # Generator Expression: https://stackoverflow.com/questions/2917372/how-to-search-a-list-of-tuples-in-python
                existing_id = next((v[0] for i, v in enumerate(existing_set)
                                    if v[1] == stock.symbol), None)

                values = {"id": existing_id,
                          "symbol": stock.symbol,
                          "name": otc_data.name,
                          "stateofincorporation": otc_data.state_of_incorporation,
                          "authorizedshares":  security_data.authorized_shares,
                          "outstandingshares": security_data.outstanding_shares,
                          "unrestrictedshares": security_data.unrestricted_shares,
                          "restrictedshares": security_data.restricted_shares,
                          "float": security_data.public_float,
                          "dtcshares": security_data.dtc_shares,
                          "tier": security_data.tier_display_name,
                          "reportingstandard": otc_data.reporting_standard,
                          "marketcap": stock.market_cap,
                          "thirtydayavgvolume": stock.thirty_days_avg_vol,
                          "iscavetemptor": security_data.is_caveat_emptor,
                          "istransferagentverified": profile_data.verified_profile if len(profile) > 0 else False,
                          "updatedate": datetime.now(),
                          "otcupdatedate": datetime.now(),
                          }

                if existing_id:
                    update_list.append(values)
                else:
                    values["insertdate"] = datetime.now()
                    insert_list.append(values)
        except Exception as e:
            print(e)

    print(f"Updating {len(update_list)} existing record(s)")
    bulk_update(update_list)
    print("Complete")

    print(f"Inserting {len(insert_list)} new record(s)")
    bulk_insert(insert_list)
    print("Complete")


def get_existing(data):
    with session_scope() as s:
        result = s.query(Stock.id, Stock.symbol).filter(
            Stock.symbol.in_(data))
        # This is extended iterable unpacking: https://www.python.org/dev/peps/pep-3132/
        result = [(id, symbol) for id, symbol, *_ in result]
        return result


def bulk_update(data):
    try:
        with session_scope() as s:
            s.bulk_update_mappings(Stock, data)
            s.commit()
    except Exception as e:
        print(e)


def bulk_insert(data):
    try:
        with session_scope() as s:
            s.bulk_insert_mappings(Stock, data)
            s.commit()
    except Exception as e:
        print(e)


def main():
    tickers = set(map(lambda x: x['symbol'], get_json()))
    otc_full_list = []
    otc_inside_list = []
    otc_profile_list = []

    complete = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for ticker in tickers:
            futures.append(executor.submit(
                otc_response, OTCMARKETS_FULL_URL+ticker, ticker, "FULL"))
            futures.append(executor.submit(
                otc_response, OTCMARKETS_INSIDE_URL+ticker, ticker, "INSIDE"))
            futures.append(executor.submit(
                otc_response, OTCMARKETS_PROFILE_BADGE_URL+ticker+'/badges?symbol='+ticker, ticker, "PROFILE_BADGE"))                
            print(f"Pulling OTC data for {ticker}")

        for future in concurrent.futures.as_completed(futures):
            try:
                if(future.result()):
                    msg, json_result, symbol, otc_type = future.result()
                    complete += 1
                    print(msg + f" {complete} of {len(futures)} completed")
                if json_result:
                    if otc_type == "FULL":
                        otc_full_list.append(otc.otc_from_dict(json_result))
                    elif otc_type == "INSIDE":
                        otc_inside_list.append(
                            otccurrent.otccurrent_from_dict(json_result))
                    elif otc_type == "PROFILE_BADGE":
                        # Profile JSON from OTC doesn't have the symbol, adding it here
                        profile = otcprofile.otcprofile_from_dict(json_result)
                        profile.symbol = symbol
                        otc_profile_list.append(profile)                            
            except Exception as e:
                print(e)

    prepare_data(otc_full_list, otc_inside_list, otc_profile_list)
    print("Done.")


if __name__ == '__main__':
    main()
