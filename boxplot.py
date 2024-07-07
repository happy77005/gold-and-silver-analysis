import pandas as pd
import matplotlib.pyplot as plt

gold_file_path = r'D:\OneDrive\Desktop\gold\gold.csv'
silver_file_path = r'D:\OneDrive\Desktop\gold\silver.csv'

gold_df = pd.read_csv(gold_file_path, parse_dates=['date'])
gold_df['date'] = pd.to_datetime(gold_df['date'], errors='coerce')
gold_df.dropna(subset=['date', 'price'], inplace=True)
gold_df.set_index('date', inplace=True)

silver_df = pd.read_csv(silver_file_path, parse_dates=['date'])
silver_df['date'] = pd.to_datetime(silver_df['date'], errors='coerce')
silver_df.dropna(subset=['date', 'price'], inplace=True)
silver_df.set_index('date', inplace=True)

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

axs[0].boxplot(gold_df['price'], labels=['Gold Price'])
axs[0].set_title('Box Plot of Gold Prices')
axs[0].set_ylabel('Price (USD)')
axs[0].grid(True)

axs[1].boxplot(silver_df['price'], labels=['Silver Price'])
axs[1].set_title('Box Plot of Silver Prices')
axs[1].set_ylabel('Price (USD)')
axs[1].grid(True)

plt.tight_layout()
plt.show()
