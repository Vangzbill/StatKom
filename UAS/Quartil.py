import csv
import statistics

with open('Walmart.csv', 'r') as file:
    reader = csv.DictReader(file)

    regresi_cols = ['Fuel_Price', 'CPI', 'Unemployment']

    store_4_stats = {}

    for col in regresi_cols:
        data = []

        for row in reader:
            if row[col] and row['Store'] == '4':
                data.append(float(row[col]))

        q1 = statistics.quantiles(data, n=4)[0]
        q2 = statistics.median(data)
        q3 = statistics.quantiles(data, n=4)[2]
        iqr = q3 - q1

        store_4_stats[col] = {
            'Q1': q1,
            'Q2': q2,
            'Q3': q3,
            'IQR': iqr
        }

        file.seek(0)
        next(reader)

    for col, stats in store_4_stats.items():
        print(f"Kolom: {col}")
        for stat, value in stats.items():
            print(f"{stat}: {value}")
        print()
