import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to the CSV file for silver prices
silver_csv_file_path = r'D:\OneDrive\Desktop\gold\silver.csv'

# Step 1: Read the CSV file into a DataFrame with date parsing and index column
silver_df = pd.read_csv(silver_csv_file_path, parse_dates=['date'], index_col='date')

# Step 2: Plot silver prices over time
plt.figure(figsize=(10, 6))
plt.plot(silver_df.index, silver_df['price'], marker='o', linestyle='-', color='silver')
plt.title('Silver Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
