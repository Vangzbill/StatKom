import pandas as pd

df = pd.read_csv('Walmart.csv')

average_cpi_holiday = df[df['Holiday_Flag'] == 1]['CPI'].mean()
average_cpi_non_holiday = df[df['Holiday_Flag'] == 0]['CPI'].mean()

print(f"Rata-rata CPI - Holiday Week: {average_cpi_holiday}")
print(f"Rata-rata CPI - Non-Holiday Week: {average_cpi_non_holiday}")
if average_cpi_holiday > average_cpi_non_holiday:
    print("CPI lebih tinggi pada holiday week.")
elif average_cpi_holiday < average_cpi_non_holiday:
    print("CPI lebih tinggi pada non-holiday week.")
else:
    print("CPI sama pada holiday week dan non-holiday week.")
