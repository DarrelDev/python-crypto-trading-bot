# 📈 Quantitative Trading Engine: Dynamic Noise Filtering Algorithm

A Python-based algorithmic trading engine designed for the **Indodax** exchange. This system implements a statistical noise-filtering mechanism to identify true market trends while mitigating false signals caused by high-frequency volatility.

> **Status:** 🟢 Active (Simulation Mode) | **Strategy:** SMA Deviation Thresholding

## 🧮 Mathematical Model

The core logic utilizes a **Dynamic Thresholding** approach to determine entry and exit points. Unlike standard Moving Average crossovers, this engine creates a "Noise Deadband" around the Simple Moving Average (SMA).

The trading bands are calculated as follows:

$$Upper Band = SMA_n \times (1 + \delta)$$
$$Lower Band = SMA_n \times (1 - \delta)$$

Where:
- $SMA_n$: Simple Moving Average over period $n$ (Default: 10).
- $\delta$: Noise Threshold Coefficient (Default: `0.0001` or 0.01%).

**Signal Logic:**
- **Long Entry (Buy):** $Price > Upper Band$ (Momentum Breakout confirmed).
- **Long Exit (Sell):** $Price < Lower Band$ (Trend Reversal confirmed).
- **Hold:** $Lower Band \le Price \le Upper Band$ (Market Noise).

## 🔥 Key Features

- **Statistical Noise Filter:** Filters out micro-volatility to prevent "whipsaw" losses during sideways markets.
- **Latency Management:** Implements API rate-limiting to ensure stable execution.
- **Risk Management:**
  - **Dynamic Take Profit:** Rides the trend until a reversal signal is detected.
  - **Stop Loss Mechanism:** Automatically exits positions when the price breaches the lower confidence band.
- **Transaction Cost Analysis:** Built-in fee simulation (0.3% maker/taker) for accurate Net PnL calculation.

## 🛠️ Technology Stack

- **Core Logic:** Python 3.10+
- **Market Data:** `ccxt` (CryptoCurrency eXchange Trading Library)
- **Data Structure:** List-based deque for O(1) time complexity on sliding window operations.

## ⚡ Execution

### Prerequisites
```bash
pip install ccxt
```
### Run Simulation
```Bash
python bot_v4.py
```

© 2026 DarrelDev. Open source for educational and research purposes.
