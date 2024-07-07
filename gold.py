import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = r'D:\OneDrive\Desktop\gold\gold.csv'
df = pd.read_csv(file_path)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop any rows with missing dates or prices
df.dropna(inplace=True)

# Convert 'price' column to float
df['price'] = df['price'].astype(float)

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['price'], marker='o', linestyle='-')
plt.title('Gold Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.tight_layout()
plt.show()
