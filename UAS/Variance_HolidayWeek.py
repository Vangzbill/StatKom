import pandas as pd

df = pd.read_csv('Walmart.csv')

holiday_sales = df[df['Holiday_Flag'] == 1]['Weekly_Sales']
non_holiday_sales = df[df['Holiday_Flag'] == 0]['Weekly_Sales']

variance_holiday = holiday_sales.var()
variance_non_holiday = non_holiday_sales.var()

print(f"Variance - Holiday Week: {variance_holiday}")
print(f"Variance - Non-Holiday Week: {variance_non_holiday}")
