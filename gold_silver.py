import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time


gold_csv_file_path = r'D:\OneDrive\Desktop\gold\gold.csv'
silver_csv_file_path = r'D:\OneDrive\Desktop\gold\silver.csv'


gold_df = pd.read_csv(gold_csv_file_path, parse_dates=['date'])
silver_df = pd.read_csv(silver_csv_file_path, parse_dates=['date'])


gold_df.dropna(subset=['date', 'price'], inplace=True)
silver_df.dropna(subset=['date', 'price'], inplace=True)


common_dates = gold_df['date'].isin(silver_df['date'])
gold_df = gold_df[common_dates].reset_index(drop=True)
silver_df = silver_df[silver_df['date'].isin(gold_df['date'])].reset_index(drop=True)

# Create empty containers for streaming simulation
gold_stream, silver_stream, dates_stream = [], [], []

plt.ion() 
fig, ax = plt.subplots(figsize=(12, 6))

# Stream the data row by row
for i in range(len(gold_df)):
    # Simulate new incoming data
    new_date = gold_df.loc[i, 'date']
    new_gold = gold_df.loc[i, 'price']
    new_silver = silver_df.loc[i, 'price']

    dates_stream.append(new_date)
    gold_stream.append(new_gold)
    silver_stream.append(new_silver)


    if len(gold_stream) > 2:  # at least 3 points needed
        pcc = np.corrcoef(gold_stream, silver_stream)[0, 1]
        print(f"{new_date.date()} → Rolling PCC: {pcc:.4f}")


    ax.clear()
    ax.plot(dates_stream, gold_stream, label="Gold", color="gold")
    ax.plot(dates_stream, silver_stream, label="Silver", color="silver")
    ax.set_title("Streaming Gold & Silver Prices")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.legend()
    ax.grid(True)
    plt.draw()
    plt.pause(0.1)

    time.sleep(0.2)  # simulate data

plt.ioff()
plt.show()
