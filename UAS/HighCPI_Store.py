import pandas as pd

df = pd.read_csv('Walmart.csv')

max_cpi_row = df[df['CPI'] == df['CPI'].max()]

print(max_cpi_row[['Store', 'CPI']])
