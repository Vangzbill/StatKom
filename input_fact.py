import csv
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-H1MMP05;DATABASE=Sales;Trusted_Connection=yes;')
cursor = conn.cursor()

region_ids = {}
cursor.execute("SELECT id_region, region_name FROM DimRegion")
rows = cursor.fetchall()
for row in rows:
    region_ids[row.region_name] = row.id_region

country_ids = {}
cursor.execute("SELECT id_country, country FROM DimCountry")
rows = cursor.fetchall()
for row in rows:
    country_ids[row.country] = row.id_country

type_ids = {}
cursor.execute("SELECT id_type, item_type FROM DimItemType")
rows = cursor.fetchall()
for row in rows:
    type_ids[row.item_type] = row.id_type

priority_ids = {}
cursor.execute("SELECT id_priority, priority, description FROM DimPriority")
rows = cursor.fetchall()
for row in rows:
    priority_ids[row.priority] = row.id_priority

metode_ids = {}
cursor.execute("SELECT id_metode, metode FROM DimMetode")
rows = cursor.fetchall()
for row in rows:
    metode_ids[row.metode] = row.id_metode

with open('Sales_Data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        region = row[0]
        country = row[1]
        item_type = row[2]
        metode = row[3]
        priority = row[4]
        order_date = row[5]
        ship_date = row[7]
        units_sold = row[8]
        unit_selling_price = row[9]

        id_region = region_ids.get(region)
        id_country = country_ids.get(country)
        id_type = type_ids.get(item_type)
        id_priority = priority_ids.get(priority)
        id_metode = metode_ids.get(metode)

        query = "INSERT INTO FactSales (id_region, id_country, id_type, id_metode, id_priority, " \
            "order_year, ship_year, unit_sold, unit_price) " \
            "VALUES (?, ?, ?, ?, ?, YEAR(?), YEAR(?), ?, ?)"

        cursor.execute(query, (id_region, id_country, id_type, id_metode,
                       id_priority, order_date, ship_date, units_sold, unit_selling_price))

        cursor.commit()
