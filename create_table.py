import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS Items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

connection.commit()
connection.close()