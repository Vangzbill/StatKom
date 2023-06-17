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
        genre = row[4]

        if genre not in unique_data:
            unique_data.add(genre)

            query = f"INSERT INTO DimGenre (genre) VALUES (?)"

            cursor.execute(query, (genre))
    conn.commit()

conn.close()
