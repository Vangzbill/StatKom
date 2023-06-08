import pyodbc
import csv

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-H1MMP05;DATABASE=DataFilms;Trusted_Connection=yes;')

with open('data_films.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        film_id = row[1]
        age = row[4]
        Netflix = row[6]
        Hulu = row[7]
        PrimeVideo = row[8]
        Disney = row[9]
        platform_id = 0
        kategori_id = 0

        if Netflix == '1' and age == '7+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 1, 1)
            cursor.commit()

        if Netflix == '1' and age == '13+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 2, 1)
            cursor.commit()

        if Netflix == '1' and age == '16+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 3, 1)
            cursor.commit()

        if Netflix == '1' and age == '18+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 4, 1)
            cursor.commit()

        if Netflix == '1' and age == '':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 5, 1)
            cursor.commit()

        if Hulu == '1' and age == '7+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 1, 2)
            cursor.commit()

        if Hulu == '1' and age == '13+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 2, 2)
            cursor.commit()

        if Hulu == '1' and age == '16+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 3, 2)
            cursor.commit()

        if Hulu == '1' and age == '18+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 4, 2)
            cursor.commit()

        if Hulu == '1' and age == '':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 5, 2)
            cursor.commit()

        if PrimeVideo == '1' and age == '7+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 1, 3)
            cursor.commit()

        if PrimeVideo == '1' and age == '13+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 2, 3)
            cursor.commit()

        if PrimeVideo == '1' and age == '16+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 3, 3)
            cursor.commit()

        if PrimeVideo == '1' and age == '18+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 4, 3)
            cursor.commit()

        if PrimeVideo == '1' and age == '':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 5, 3)
            cursor.commit()

        if Disney == '1' and age == '7+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 1, 4)
            cursor.commit()

        if Disney == '1' and age == '13+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 2, 4)
            cursor.commit()

        if Disney == '1' and age == '16+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 3, 4)
            cursor.commit()

        if Disney == '1' and age == '18+':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 4, 4)
            cursor.commit()

        if Disney == '1' and age == '':
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO FactPenayangan (film_id, kategori_id, platform_id) VALUES (?, ?, ?)", film_id, 5, 4)
            cursor.commit()
