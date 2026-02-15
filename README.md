# 🚀 Algo-Trading Bot V4 (Python)

A lightweight, automated cryptocurrency trading bot designed for the **Indodax** exchange. Built with Python and the **CCXT** library, this bot utilizes a **threshold-based strategy** to filter market noise and execute trades based on real-time moving averages.

> **Status:** 🟢 Active (Simulation Mode)

## 🔥 Key Features

- **Smart Noise Filtering:** Uses a dynamic threshold (`0.01%`) to ignore minor price fluctuations and prevent over-trading (whipsaw).
- **Moving Average Logic:** Makes decisions based on a 10-period moving average rather than raw instantaneous prices.
- **Risk Management:**
  - **Dynamic Take Profit:** Automatically sells when price breaks the upper resistance.
  - **Stop Loss Protection:** Triggers a sell order if the price drops below the safety margin to minimize losses.
- **Fee Simulation:** Includes a built-in calculator for exchange fees (0.3%) to provide realistic Net Profit/Loss (PnL) estimates.
- **Real-Time Logging:** Displays live transaction data, profit tracking, and signal status directly in the terminal.

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Core Library:** `ccxt` (CryptoCurrency eXchange Trading Library)
- **Environment:** Cross-Platform (Windows/Linux Compatible)
  
## ⚡ How It Works (The Logic)

1.  **Fetch Data:** Pulls real-time `BTC/IDR` ticker data from Indodax via API.
2.  **Calculate Average:** Stores the last 10 price points to calculate a Simple Moving Average (SMA).
3.  **Determine Bands:** Sets dynamic Upper and Lower bands based on the configured threshold.
4.  **Execute Trade:**
    - **BUY:** When price > Upper Band (Momentum Breakout).
    - **SELL:** When price < Lower Band (Panic/Correction).
    - **HOLD:** When price is within the "Noise Zone" (Deadband).

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed. Then install the required library:

```bash
pip install ccxt
```
Usage
Run the bot directly from your terminal:

```Bash
python bot_v4.py
```
Note: By default, the bot runs in Simulation Mode with a dummy balance of IDR 100,000,000. To go live, configure your API Keys in the environment variables (Do not hardcode keys).

⚠️ Disclaimer
This project is for educational purposes only. Cryptocurrency trading involves high risk. I am not responsible for any financial losses incurred while using this software. Always DYOR (Do Your Own Research) and test thoroughly before using real money.

Built with ❤️ by a 15 y/o Python Developer.
