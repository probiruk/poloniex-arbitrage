import func_arbitrage
import json
import time
from colorama import Fore

# Set Variables
coin_price_url = "https://poloniex.com/public?command=returnTicker"

"""
    Step 0: Finding coins which can be traded
    Exchange: Poloniex
    https://docs.legacy.poloniex.com/#introduction
"""
def step_0():
    # Extract list of coins and prices from Exchange
    coin_json = func_arbitrage.get_coin_ticker(coin_price_url)

    # Loop through each objects and find the tradeable pairs
    coin_list = func_arbitrage.collect_tradeables(coin_json)

    # Return list of tradeable coins
    return coin_list

"""
    Step 1: Structuring Triangular Pairs
    Calculation Only
"""
def step_1(coin_list):
    # Structure the list of tradeable triangular arbitrage pairs
    structured_list = func_arbitrage.structure_triangular_pairs(coin_list)

    # Save structure list
    with open("structured_triangular_pairs.json", "w") as fp:
        json.dump(structured_list, fp)

"""
    Step 2: Calculate Surface Arbitrage Opportunities
    Exchange: Poloniex
    https://docs.legacy.poloniex.com/#introduction
"""

def step_2():
    # Get Structured Pairs
    with open("structured_triangular_pairs.json") as json_file:
        structured_pairs = json.load(json_file)

    print(len(structured_pairs))

    # Get Latest Surface Prices
    prices_json = func_arbitrage.get_coin_ticker(coin_price_url)
    
    # Loop Through and Stricture Price Information
    for t_pair in structured_pairs:
        prices_dict = func_arbitrage.get_price_for_t_pair(t_pair, prices_json)
        surface_arb = func_arbitrage.calc_triangular_arb_surface_rate(t_pair, prices_dict)
        if len(surface_arb) > 1:
            print(Fore.RED + str(surface_arb))
            real_rate_arb = func_arbitrage.get_depth_from_orderbook(surface_arb)

""" MAIN """
if __name__ == "__main__":
    # coin_list = step_0()
    # structured_pairs= step_1(coin_list)
        step_2()
