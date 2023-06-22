import pandas as pd
from scipy.stats import kstest, norm

df = pd.read_csv('Walmart.csv')

weekly_sales_data = df['Weekly_Sales']
fuel_price_data = df['Fuel_Price']

ks_statistic_weekly_sales, p_value_weekly_sales = kstest(
    weekly_sales_data, 'norm')
ks_statistic_fuel_price, p_value_fuel_price = kstest(fuel_price_data, 'norm')

alpha = 0.05
critical_value = norm.ppf(1 - alpha / 2)

print("Uji Normalitas - Weekly Sales:")
print(f"KS Statistic: {ks_statistic_weekly_sales}")
print(f"P-Value: {p_value_weekly_sales}")
if ks_statistic_weekly_sales > critical_value or p_value_weekly_sales > alpha:
    print("Berdasarkan Distribusi tidak normal")
else:
    print("Berdasarkan Distribusi normal")

print("\nUji Normalitas - Fuel Price:")
print(f"KS Statistic: {ks_statistic_fuel_price}")
print(f"P-Value: {p_value_fuel_price}")
if ks_statistic_fuel_price > critical_value or p_value_fuel_price > alpha:
    print("Berdasarkan Distribusi tidak normal")
else:
    print("Berdasarkan Distribusi normal")
