import pyodbc
import csv

conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=DESKTOP-H1MMP05;DATABASE=DataFilms;Trusted_Connection=yes;')

with open('DisneyMoviesDataset.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    
    for row in reader:
        id = row[0]
        title = row[1]
        running_time = row[7]
        budget = row[8]
        interest = row[9]
        release_date = row[10]
        rating = row[11]
        
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO dimFilm (id, title, running_time, budget, interest, release_date, rating) VALUES (?, ?, ?, ?, ?, ?, ?)", id, title, running_time, budget, interest, release_date, rating)
        cursor.commit()
        
        