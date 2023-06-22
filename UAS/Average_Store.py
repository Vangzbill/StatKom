import pandas as pd

df = pd.read_csv('Walmart.csv')

average_sales_per_store = df.groupby('Store')['Weekly_Sales'].mean()

print(average_sales_per_store)
