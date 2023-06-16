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
        priority = row[4]

        if priority not in unique_data:
            unique_data.add(priority)

            query = f"INSERT INTO DimPriority (priority) VALUES (?)"

            cursor.execute(query, (priority))

    conn.commit()

conn.close()
