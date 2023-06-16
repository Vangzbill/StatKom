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
        country = row[1]

        if country not in unique_data:
            unique_data.add(country)

            query = f"INSERT INTO DimCountry (country) VALUES (?)"

            cursor.execute(query, (country))

    conn.commit()

conn.close()
