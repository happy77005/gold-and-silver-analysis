import pandas as pd
import numpy as np
gold_csv_file_path = r'D:\OneDrive\Desktop\gold\gold.csv'
silver_csv_file_path = r'D:\OneDrive\Desktop\gold\silver.csv'

gold_df = pd.read_csv(gold_csv_file_path, parse_dates=['date'])
gold_df['date'] = pd.to_datetime(gold_df['date'], errors='coerce')

gold_df.dropna(subset=['date', 'price'], inplace=True)
gold_df.set_index('date', inplace=True)

silver_df = pd.read_csv(silver_csv_file_path, parse_dates=['date'])
silver_df['date'] = pd.to_datetime(silver_df['date'], errors='coerce')
silver_df.dropna(subset=['date', 'price'], inplace=True)
silver_df.set_index('date', inplace=True)

common_dates = gold_df.index.intersection(silver_df.index)

gold_prices = gold_df.loc[common_dates, 'price']
silver_prices = silver_df.loc[common_dates, 'price']
pcc = np.corrcoef(gold_prices, silver_prices)[0, 1]

print(f"Pearson Correlation Coefficient between Gold and Silver Prices: {pcc:.4f}")
