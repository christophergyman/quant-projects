import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

    # Fetch S&P 500 historical data
if __name__ == "__main__":
    ticker = "^GSPC"
    data = yf.download(ticker, start="2010-01-01", end="2024-01-01")

    # Use "Close" instead of "Adj Close" if needed
    prices = data.get("Adj Close", data["Close"])  # Fallback to "Close" if "Adj Close" is missing

    # Calculate daily returns
    returns = prices.pct_change().dropna()

    # Monte Carlo simulation parameters
    num_simulations = 1000
    num_days = 252  # One trading year

    # Generate random daily returns based on historical mean & std dev
    mean_return = returns.mean()
    std_dev = returns.std()

    simulations = np.zeros((num_days, num_simulations))

    for i in range(num_simulations):
        random_returns = np.random.normal(mean_return, std_dev, num_days)
        
        # Start from last known price
        price_series = np.zeros(num_days)  
        price_series[0] = prices.iloc[-1]

        for j in range(1, num_days):
            price_series[j] = price_series[j - 1] * (1 + random_returns[j - 1])

        simulations[:, i] = price_series  # Ensure it's a 1D NumPy array

    # Plot results
    plt.figure(figsize=(12, 6))
    plt.plot(simulations, alpha=0.1, color="blue")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.title(f"Monte Carlo Simulation of {ticker} Future Prices")
    plt.show()
