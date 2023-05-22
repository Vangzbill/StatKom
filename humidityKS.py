import pandas as pd
from scipy.stats import kstest, norm

# Baca data dari file CSV
data = pd.read_csv('weatherHistory.csv')

# Ambil kolom 'Humidity' dari data
humidity_data = data['Humidity']

# Hitung mean dan standard deviation dari data 'Humidity'
mean = humidity_data.mean()
std_dev = humidity_data.std()

# Lakukan uji KS
ks_statistic, p_value = kstest(humidity_data, 'norm', args=(mean, std_dev))

# Tentukan alpha (p-value threshold) berdasarkan tingkat kepercayaan 99%
alpha = 1 - 0.99

# Cetak hasil uji KS
if p_value > alpha:
    print("Humidity terdistribusi normal")
else:
    print("Humidity tidak terdistribusi normal")
print("Nilai KS:", ks_statistic)
