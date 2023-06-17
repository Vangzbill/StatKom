import csv
import pyodbc


conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-H1MMP05;DATABASE=Sales;Trusted_Connection=yes;')

cursor = conn.cursor()

with open('Sales_Data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        making_cost = row[10]

        query = "UPDATE FactSales SET making_cost = ?"

        cursor.execute(query, (making_cost,))

    conn.commit()
