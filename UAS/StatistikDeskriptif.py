import csv
import statistics

with open('Walmart.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    regresi_cols = ['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
    
    descriptive_stats = {}
    
    for col in regresi_cols:
        data = []
        
        for row in reader:
            if row[col]:
                data.append(float(row[col]))
        
        descriptive_stats[col] = {
            'Mean': statistics.mean(data),
            'Median': statistics.median(data),
            'Standard Deviation': statistics.stdev(data),
            'Variance': statistics.variance(data)
        }
        
        file.seek(0)
        next(reader)
    
    for col, stats in descriptive_stats.items():
        print(f"Column: {col}")
        for stat, value in stats.items():
            print(f"{stat}: {value}")
        print()
