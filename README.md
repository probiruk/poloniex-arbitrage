# Crypto Triangular Arbitrage Bot

## Overview
This project implements a **triangular arbitrage** strategy for cryptocurrency trading on the **Poloniex exchange**. The script scans tradeable currency pairs, structures potential arbitrage loops, and calculates profit/loss opportunities based on real-time order book data.

## Features
- **Fetch real-time market data** from Poloniex API
- **Identify tradeable currency pairs** that are not frozen or post-only
- **Structure potential triangular arbitrage opportunities**
- **Calculate profitability** based on real-time bid/ask prices
- **Assess arbitrage depth** using order book liquidity

## How It Works
1. **Fetch market data**: The script pulls live currency pair prices from Poloniex.
2. **Identify valid pairs**: It filters out non-tradeable pairs.
3. **Structure arbitrage loops**: The script finds three-pair combinations where arbitrage might be possible.
4. **Analyze pricing and liquidity**: It calculates bid/ask spreads and estimates potential profit.
5. **Simulate trades**: The script runs forward and reverse simulations to determine profitability.

## Installation
### Requirements
- Python 3.x
- Required libraries: `requests`, `json`, `time` and `colorama`

### Setup
Clone the repository:
```bash
git clone https://github.com/yourusername/crypto-triangular-arbitrage.git
cd crypto-triangular-arbitrage
```

Install the required libraries above:
```bash
pip install requests
...
```

## Usage
Run the script to analyze triangular arbitrage opportunities:
```bash
python main.py
```

## Example Output
```json
{
  "contract_1": "BTC_USDT",
  "contract_2": "ETH_BTC",
  "contract_3": "ETH_USDT",
  "profit_loss": 0.0025,
  "real_rate_perc": 0.45
}
```
This output indicates a potential **0.45% profit** if the arbitrage trade is executed successfully.

## Disclaimer
This script is for **educational and research purposes only**. Cryptocurrency trading involves financial risk. Always conduct your own analysis before making trading decisions.

## License
This project is licensed under the MIT License.
