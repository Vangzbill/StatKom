import csv
import pyodbc

# Membuka koneksi ke database
conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-H1MMP05;DATABASE=VGSales;Trusted_Connection=yes;')
cursor = conn.cursor()

# Membuat kamus untuk memetakan nilai genre, platform, dan publisher dengan ID yang sesuai
id_genre_dict = {}
id_platform_dict = {}
id_publisher_dict = {}

# Membaca data dari tabel DimGenre dan memasukkannya ke kamus id_genre_dict
cursor.execute("SELECT id_genre, genre FROM DimGenre")
rows = cursor.fetchall()
for row in rows:
    id_genre_dict[row.genre] = row.id_genre

# Membaca data dari tabel DimPlatform dan memasukkannya ke kamus id_platform_dict
cursor.execute("SELECT id_platform, platform FROM DimPlatform")
rows = cursor.fetchall()
for row in rows:
    id_platform_dict[row.platform] = row.id_platform

# Membaca data dari tabel DimPublisher dan memasukkannya ke kamus id_publisher_dict
cursor.execute("SELECT id_publisher, publisher FROM DimPublisher")
rows = cursor.fetchall()
for row in rows:
    id_publisher_dict[row.publisher] = row.id_publisher

# Membuka file CSV
with open('vgsales.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Melewati baris header

    # Mengimpor data ke tabel FactVideoGameSales
    for row in reader:
        name = row[1]
        platform = row[2]
        year = row[3]
        genre = row[4]
        publisher = row[5]
        na_sales = row[6]
        eu_sales = row[7]
        jp_sales = row[8]
        other_sales = row[9]
        global_sales = row[10]

        # Mengonversi nilai sales menjadi float atau None jika 'N/A'
        na_sales = float(na_sales) if na_sales != 'N/A' else None
        eu_sales = float(eu_sales) if eu_sales != 'N/A' else None
        jp_sales = float(jp_sales) if jp_sales != 'N/A' else None
        other_sales = float(other_sales) if other_sales != 'N/A' else None
        global_sales = float(global_sales) if global_sales != 'N/A' else None

        # Mendapatkan ID genre, platform, dan publisher dari kamus
        id_genre = id_genre_dict.get(genre)
        id_platform = id_platform_dict.get(platform)
        id_publisher = id_publisher_dict.get(publisher)

        # Menjalankan pernyataan SQL untuk memasukkan data ke tabel FactVideoGameSales
        query = "INSERT INTO FactVideoGameSales (name, id_platform, year, id_genre, id_publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales) " \
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (name, id_platform, year, id_genre, id_publisher,
                       na_sales, eu_sales, jp_sales, other_sales, global_sales))
        cursor.commit()

# Menutup koneksi ke database
cursor.close()
conn.close()
