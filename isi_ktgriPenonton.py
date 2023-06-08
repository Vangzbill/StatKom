import pyodbc
import csv

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-H1MMP05;DATABASE=DataFilms;Trusted_Connection=yes;')

with open('data_films.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        age = row[4]
        kategori_id = 0

        if age == '7+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (kategori_id) VALUES (?)", 1)
            cursor.commit()

        if age == '13+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (kategori_id) VALUES (?)", 2)
            cursor.commit()

        if age == '16+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (kategori_id) VALUES (?)", 3)
            cursor.commit()

        if age == '18+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (kategori_id) VALUES (?)", 4)
            cursor.commit()

        if age == '':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (kategori_id) VALUES (?)", 5)
            cursor.commit()
