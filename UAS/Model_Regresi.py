import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('Walmart.csv')

x = df['Fuel_Price']
y = df['Weekly_Sales']

x = sm.add_constant(x)

model = sm.OLS(y, x)

results = model.fit()

print(results.summary())
