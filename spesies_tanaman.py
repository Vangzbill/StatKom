import scipy.stats as stats
import math

# Nilai yang diberikan
sample_mean = 15  # Rata-rata sampel
population_variance = 16  # Varians populasi
sample_size = 25  # Ukuran sampel

# Menghitung simpangan baku populasi
population_std_dev = math.sqrt(population_variance)

# Menghitung skor z untuk tingkat kepercayaan 95%
confidence_level = 0.95
alpha = 1 - confidence_level
z_score = stats.norm.ppf(1 - alpha/2)

# Menghitung interval kepercayaan
margin_of_error = z_score * (population_std_dev / math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

# Menampilkan hasil
print("Rentang nilai rata-rata populasi dengan tingkat kepercayaan 95%:")
print("Batas bawah:", confidence_interval[0])
print("Batas atas:", confidence_interval[1])
