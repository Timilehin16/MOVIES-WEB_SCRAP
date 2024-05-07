import sqlite3


def create_database():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
                        name TEXT,
                        image TEXT,
                        url TEXT,
                        detail TEXT)''')
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error creating database:", e)

def insert_data(movie_data):
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO movies VALUES(?, ?, ?, ?)", movie_data)
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error inserting data into database:", e)
        
        
