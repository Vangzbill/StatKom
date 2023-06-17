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
        publisher = row[5]

        if publisher not in unique_data:
            unique_data.add(publisher)

            query = f"INSERT INTO DimPublisher (publisher) VALUES (?)"

            cursor.execute(query, (publisher))

    conn.commit()
conn.close()
