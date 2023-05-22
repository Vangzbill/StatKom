import scipy.stats as stats

# Menghitung peluang menggunakan fungsi kumulatif distribusi normal (CDF)
mean = 200  # Rata-rata
std_dev = 20  # Simpangan baku
x = 204  # Nilai batas atas

z = (x - mean) / std_dev  # Menghitung z-score

# Menggunakan CDF untuk menghitung peluang
probability = stats.norm.cdf(z)

# Menghitung peluang bahwa 100 pria memiliki kolesterol di bawah 204 mg/dL
probability_100_pria = probability ** 100

print("Peluang bahwa 100 pria memiliki kolesterol di bawah 204 mg/dL:", probability_100_pria)
