import math
import numpy as np
from scipy.stats import f

def hitung_simpangan_baku(data):
    n = len(data)
    mean = sum(data) / n
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / n
    std_dev = math.sqrt(variance)
    return std_dev

array_tool = [32, 31, 32, 32, 33, 35, 32, 34, 31, 29, 36, 30, 33]
array_no_tool = [29, 30, 27, 28, 26, 27, 31, 27, 26, 28, 27, 24, 25]

simpangan_baku = hitung_simpangan_baku(array_tool)
print("Simpangan Baku Dengan Tool:", simpangan_baku)
simpangan_baku_no_tool = hitung_simpangan_baku(array_no_tool)
print("Simpangan Baku Tanpa Tool:", simpangan_baku_no_tool)
print("=====================================")

def uji_hartley(*arrays):
    num_groups = len(arrays)
    num_values = [len(arr) for arr in arrays]
    
    # Hitung sum of squares (SS) untuk masing-masing grup
    ss_groups = [np.sum(np.square(arr)) for arr in arrays]
    
    # Hitung SS antara grup
    ss_between = np.sum(ss_groups)
    
    # Hitung SS dalam grup
    ss_within = sum([(num_values[i] - 1) * np.var(arr) for i, arr in enumerate(arrays)])
    
    # Hitung F-statistic
    f_statistic = (ss_between / (num_groups - 1)) / (ss_within / (sum(num_values) - num_groups))
    
    # Hitung nilai p-value
    p_value = 1 - f.cdf(f_statistic, num_groups - 1, sum(num_values) - num_groups)
    
    return f_statistic, p_value

f_stat, p_val = uji_hartley(array_tool, array_no_tool)
print("F-Statistic:", f_stat)
print("P-Value:", p_val)

alpha = 0.05

if p_val > alpha:
    print("Data homogen")
else:
    print("Data tidak homogen")
