import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import os

# Paths (absolute paths from your directory listing)
base_path = r"C:\Users\harip\Desktop\pro\projects\p&s project"
gold_csv_file = os.path.join(base_path, "gold.csv")
silver_csv_file = os.path.join(base_path, "silver.csv")

# Load datasets
gold_df = pd.read_csv(gold_csv_file)
silver_df = pd.read_csv(silver_csv_file)

# Force convert 'date' to datetime in both
gold_df['date'] = pd.to_datetime(gold_df['date'], errors='coerce')
silver_df['date'] = pd.to_datetime(silver_df['date'], errors='coerce')

# Drop rows with missing date or price
gold_df.dropna(subset=['date', 'price'], inplace=True)
silver_df.dropna(subset=['date', 'price'], inplace=True)

# Merge on common dates
df = pd.merge(gold_df, silver_df, on="date", suffixes=('_gold', '_silver'))
df.sort_values("date", inplace=True)

# Setup matplotlib for live updates
plt.ion()
fig, ax = plt.subplots(figsize=(12, 6))

gold_prices = []
silver_prices = []
dates = []

# Simulate streaming row by row
for _, row in df.iterrows():
    dates.append(row['date'])
    gold_prices.append(row['price_gold'])
    silver_prices.append(row['price_silver'])

    ax.clear()
    ax.plot(dates, gold_prices, label="Gold", color="gold")
    ax.plot(dates, silver_prices, label="Silver", color="silver")
    ax.set_title("Streaming Gold & Silver Prices")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.legend()
    ax.grid(True)

    # Calculate Pearson Correlation on current data
    if len(gold_prices) > 5:  # wait until enough points
        pcc = np.corrcoef(gold_prices, silver_prices)[0, 1]
        ax.text(0.02, 0.95, f"Pearson Corr: {pcc:.4f}",
                transform=ax.transAxes, fontsize=12,
                bbox=dict(facecolor="white", alpha=0.7))

    plt.draw()
    plt.pause(0.2)  # simulate streaming delay

plt.ioff()
plt.show()
