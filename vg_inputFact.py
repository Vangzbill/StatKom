import csv
import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-H1MMP05;DATABASE=VGSales;Trusted_Connection=yes;')
cursor = conn.cursor()

id_genre_dict = {}
id_platform_dict = {}
id_publisher_dict = {}

cursor.execute("SELECT id_genre, genre FROM DimGenre")
rows = cursor.fetchall()
for row in rows:
    id_genre_dict[row.genre] = row.id_genre

cursor.execute("SELECT id_platform, platform FROM DimPlatform")
rows = cursor.fetchall()
for row in rows:
    id_platform_dict[row.platform] = row.id_platform

cursor.execute("SELECT id_publisher, publisher FROM DimPublisher")
rows = cursor.fetchall()
for row in rows:
    id_publisher_dict[row.publisher] = row.id_publisher


with open('vgsales.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row['Name']
        platform = row['Platform']
        year = row['Year']
        genre = row['Genre']
        publisher = row['Publisher']
        na_sales = row['NA_Sales']
        eu_sales = row['EU_Sales']
        jp_sales = row['JP_Sales']
        other_sales = row['Other_Sales']
        global_sales = row['Global_Sales']

        try:
            na_sales = float(na_sales)
        except ValueError:
            na_sales = 0.0

        try:
            eu_sales = float(eu_sales)
        except ValueError:
            eu_sales = 0.0

        try:
            jp_sales = float(jp_sales)
        except ValueError:
            jp_sales = 0.0

        try:
            other_sales = float(other_sales)
        except ValueError:
            other_sales = 0.0

        try:
            global_sales = float(global_sales)
        except ValueError:
            global_sales = 0.0

        id_genre = id_genre_dict.get(genre)
        id_platform = id_platform_dict.get(platform)
        id_publisher = id_publisher_dict.get(publisher)

        query = "INSERT INTO FactVideoGameSales (name, id_platform, year, id_genre, id_publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales) " \
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (name, id_platform, year, id_genre, id_publisher,
                       na_sales, eu_sales, jp_sales, other_sales, global_sales))
        cursor.commit()

cursor.close()
conn.close()
