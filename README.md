# 📈 Momentum Trading Strategy using EMA Crossover

## 🚀 Overview
This project implements a systematic momentum-based trading strategy using Exponential Moving Average (EMA) crossovers. It is designed as part of my quantitative finance internship portfolio, focusing on building rule-based, data-driven trading systems.

The strategy captures short-term trends and identifies optimal entry/exit points using price-action confirmation.

---

## 🧠 Strategy Concept

The core idea is based on trend-following momentum:

- A fast EMA (8-period) reacts quickly to price changes  
- A slow EMA (21-period) represents the broader trend  

### 📌 Trading Logic

#### ✅ Long (Buy)
- Condition: EMA(8) > EMA(21) → Uptrend  
- Entry: Buy on pullbacks toward EMA(8)  

#### ❌ Short (Sell)
- Condition: EMA(8) < EMA(21) → Downtrend  
- Entry: Sell on rallies toward EMA(8)  

---

## 📊 Mathematical Foundation

EMA is calculated as:

EMA_t = α × Price_t + (1 − α) × EMA_(t−1)

Where:
- α = 2 / (n + 1)  
- n = lookback period (8 or 21)

---

## 🛠️ Features

- EMA (8 & 21) computation  
- Signal generation (Buy/Sell logic)  
- Backtesting framework  
- Performance metrics:
  - Cumulative Returns  
  - Sharpe Ratio  
  - Maximum Drawdown  
- Modular and scalable code structure  

---

## 🧪 Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib / Plotly  
- yfinance / NSE APIs  

---

## 📂 Project Structure

mavgsys/
│── data/                # Historical price data  
│── strategy/            # EMA strategy logic  
│── backtest/            # Backtesting framework  
│── results/             # Performance outputs  
│── notebooks/           # Research & experiments  
│── README.md  

---

## 📈 Workflow

1. Load historical price data  
2. Compute EMA(8) and EMA(21)  
3. Generate trading signals  
4. Run backtest  
5. Evaluate performance  

---

## ⚠️ Assumptions & Limitations

- No transaction costs or slippage included  
- Performs best in trending markets  
- May underperform in sideways markets  

---

## 🔮 Future Enhancements

- Risk management (Stop-loss, position sizing)  
- Transaction cost modeling  
- Multi-asset portfolio testing  
- Parameter optimization  
- Live trading integration (e.g., Zerodha API)  
- Additional indicators (RSI, volume filters)  

---

## 📌 Learning Outcome

This project demonstrates:
- Quantitative thinking  
- Strategy design and validation  
- Data analysis and backtesting  
- Financial market understanding  

---

## 🤝 Contributions

Open to improvements and suggestions.

---

## ⚠️ Disclaimer

This project is for educational purposes only and does not constitute financial advice.