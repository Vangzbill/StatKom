import pandas as pd
from scipy.stats import kstest, norm

data = pd.read_csv('weatherHistory.csv') 

# Ambil kolom 'Temperature' dari data
temperature_data = data['Temperature (C)']

# Hitung mean dan standard deviation dari data 'Temperature'
mean = temperature_data.mean()
std_dev = temperature_data.std()

# Lakukan uji KS
ks_statistic, p_value = kstest(temperature_data, 'norm', args=(mean, std_dev))

# Tentukan alpha (p-value threshold)
alpha = 0.05

# Cetak hasil uji KS
if p_value > alpha:
    print("Temperature terdistribusi normal")
else:
    print("Temperature tidak terdistribusi normal")
print("Nilai KS:", ks_statistic)
