import pandas as pd

df = pd.read_csv('Walmart.csv')

correlations = df[['Store', 'Holiday_Flag', 'Temperature',
                   'Fuel_Price', 'CPI', 'Unemployment', 'Weekly_Sales']].corr()
weekly_sales_correlation = correlations['Weekly_Sales']

print("Korelasi antara variabel independen dengan Weekly_Sales:")
print(weekly_sales_correlation)
