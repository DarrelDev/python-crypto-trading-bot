#!/usr/bin/env python3
"""
Crypto Algo-Trading Bot V4 (Simulation Mode)
Author: DarrelDev
Description: 
    Automated trading script utilizing Simple Moving Average (SMA) 
    logic with a dynamic noise threshold (deadband) to filter market volatility.
    Designed for the Indodax exchange via CCXT.
"""

import ccxt
import time
from datetime import datetime
import sys

# --- CONFIGURATION (The Control Panel) ---
PAIR = 'BTC/IDR'
TIMEFRAME_WINDOW = 10         # SMA Period (Moving Average length)
NOISE_THRESHOLD = 0.0001      # 0.01% deviation required to trigger signal
TRADING_FEE = 0.003           # 0.3% exchange fee per transaction
SIMULATION_BALANCE_IDR = 100_000_000  # Initial Capital: IDR 100 Million

# --- INITIALIZATION ---
print(">>> QUANTITATIVE ENGINE INITIALIZED: Dynamic Thresholding Active")
print(f"Target Pair: {PAIR}")
print(f"Initial Capital: IDR {SIMULATION_BALANCE_IDR:,.0f}")
print("-------------------------------------------------")

try:
    exchange = ccxt.indodax()
    # Safety Check: Ensure connection works
    exchange.load_markets()
    print(">> Connection to Indodax API: ESTABLISHED")
except Exception as e:
    print(f">> CRITICAL ERROR: Could not connect to exchange. {e}")
    sys.exit()

# State Variables
price_history = []
balance_idr = SIMULATION_BALANCE_IDR
balance_crypto = 0.0
market_position = "CASH"  # Options: "CASH" or "INVESTED"

# --- MAIN ENGINE LOOP ---
while True:
    try:
        # 1. DATA ACQUISITION
        ticker = exchange.fetch_ticker(PAIR)
        current_price = float(ticker['last'])
        timestamp = datetime.now().strftime("%H:%M:%S")

        # 2. DATA PROCESSING (Moving Average Logic)
        price_history.append(current_price)
        
        # Maintain buffer size based on window
        if len(price_history) > TIMEFRAME_WINDOW:
            price_history.pop(0)

        # 3. ANALYSIS & DECISION MAKING
        if len(price_history) >= TIMEFRAME_WINDOW:
            # Calculate SMA (Simple Moving Average)
            sma = sum(price_history) / len(price_history)
            
            # Define Dynamic Bands (The "Physics" of the bot)
            upper_band = sma * (1 + NOISE_THRESHOLD)
            lower_band = sma * (1 - NOISE_THRESHOLD)

            # Calculate Deviation for visualization
            deviation = current_price - sma
            
            print(f"[{timestamp}] Price: {current_price:,.0f} | SMA: {sma:,.0f} | Status: {market_position}")

            # --- TRADING LOGIC ---
            
            # SIGNAL: MOMENTUM BREAKOUT (Buy)
            # Logic: Price breaks above the Upper Band -> Uptrend confirmed
            if current_price > upper_band and market_position == "CASH":
                print("\n   >>> 🟢 SIGNAL DETECTED: MOMENTUM BUY")
                
                # Calculate Fees & Net Volume
                gross_cost = balance_idr
                fee_cost = gross_cost * TRADING_FEE
                net_capital = gross_cost - fee_cost
                
                # Execute Virtual Order
                balance_crypto = net_capital / current_price
                balance_idr = 0
                market_position = "INVESTED"
                
                print(f"       [EXECUTION] BUY BTC at {current_price:,.0f}")
                print(f"       [ASSET] Volume: {balance_crypto:.6f} BTC | Fee: IDR {fee_cost:,.0f}\n")

            # SIGNAL: PANIC DUMP / CORRECTION (Sell)
            # Logic: Price drops below Lower Band -> Downtrend confirmed
            elif current_price < lower_band and market_position == "INVESTED":
                print("\n   >>> 🔴 SIGNAL DETECTED: STOP LOSS / TAKE PROFIT")
                
                # Calculate Revenue
                gross_revenue = balance_crypto * current_price
                fee_cost = gross_revenue * TRADING_FEE
                balance_idr = gross_revenue - fee_cost
                
                balance_crypto = 0
                market_position = "CASH"
                
                # PnL Calculation
                total_pnl = balance_idr - SIMULATION_BALANCE_IDR
                print(f"       [EXECUTION] SELL BTC at {current_price:,.0f}")
                print(f"       [RESULT] Net Balance: IDR {balance_idr:,.0f} | Fee: IDR {fee_cost:,.0f}")
                print(f"       [PERFORMANCE] Total PnL: IDR {total_pnl:,.0f}\n")
            
            # SIGNAL: NOISE / DEADBAND (Hold)
            else:
                # Physics: If price is within the threshold, it's just noise.
                print(f"   -> HOLD: Volatility within noise threshold ({NOISE_THRESHOLD*100}%). No action.")
        
        else:
            print(f"[{timestamp}] Calibrating data... ({len(price_history)}/{TIMEFRAME_WINDOW})")

        # 4. LATENCY MANAGEMENT
        # Don't spam the API. Wait 3 seconds.
        time.sleep(3)

    except Exception as e:
        print(f"[ERROR] Engine Glitch: {e}")

        time.sleep(5)

