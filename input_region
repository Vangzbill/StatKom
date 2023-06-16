import csv
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-H1MMP05;DATABASE=Sales;Trusted_Connection=yes;')

cursor = conn.cursor()

with open('Sales_Data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    unique_data = set()
    for row in reader:
        region = row[0]

        if region not in unique_data:
            unique_data.add(region)

            query = f"INSERT INTO DimRegion (region_name) VALUES (?)"

            cursor.execute(query, (region))

    conn.commit()

conn.close()
