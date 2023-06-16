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
        item = row[2]

        if item not in unique_data:
            unique_data.add(item)

            query = f"INSERT INTO DimItemType (item_type) VALUES (?)"

            cursor.execute(query, (item))

    conn.commit()

conn.close()
