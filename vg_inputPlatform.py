import csv
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-H1MMP05;DATABASE=VGSales;Trusted_Connection=yes;')

cursor = conn.cursor()

with open('vgsales.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    unique_data = set()

    for row in reader:
        platform = row[2]

        if platform not in unique_data:
            unique_data.add(platform)

            query = f"INSERT INTO DimPlatform (platform) VALUES (?)"

            cursor.execute(query, (platform))
    conn.commit()

conn.close()
