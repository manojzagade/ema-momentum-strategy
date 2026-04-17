import os
import matplotlib.pyplot as plt

from src.dataloader import load_data
from src.indicators import add_indicators
from src.signals import generate_signals
from src.backtest import backtest
from src.performance import calculate_performance


# Ensure results folder exists
os.makedirs("results", exist_ok=True)


def run(symbol):
    print(f"\nRunning for: {symbol}")

    df = load_data(symbol)
    df = add_indicators(df)
    df = generate_signals(df)
    df = backtest(df)

    metrics = calculate_performance(df)

    print("\nPerformance:")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")

    # Save equity curve
    plt.figure()
    plt.plot(df['equity_curve'])
    plt.title(f"Equity Curve - {symbol}")
    plt.xlabel("Date")
    plt.ylabel("Equity")
    plt.tight_layout()
    plt.savefig(f"results/{symbol}_equity.png")
    plt.close()

    return df


if __name__ == "__main__":
    symbols = ["^NSEI", "RELIANCE.NS", "TCS.NS"]

    for sym in symbols:
        run(sym)

    print("\nFinished running all assets.")