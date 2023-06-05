import pyodbc
import csv

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-H1MMP05;DATABASE=DataFilms;Trusted_Connection=yes;')


with open('data_films.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header if needed
    for row in reader:
        # Ambil kolom yang diinginkan menggunakan indeks kolom
        ID = row[1]
        Title = row[2]
        Year = row[3]
        Age = row[4]
        RottenTomatoes = row[5]
        # Lakukan operasi lain sesuai kebutuhan

        with conn.cursor() as cursor:
            sql = "INSERT INTO Films (ID, Title, Year, Age, RottenTomatoes) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(sql, (ID, Title, Year, Age, RottenTomatoes))
            conn.commit()


conn.close()
