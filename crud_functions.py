import sqlite3

from django.template.defaultfilters import title
from numpy.ma.core import append

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
);
''')

initiate_db()

# cursor.execute("CREATE INDEX IF NOT EXISTS id ON Products (id)")
# for i in range(1, 5):
#      cursor.execute("INSERT INTO Products (title, description, price)"
#                     " VALUES (?, ?, ?)", (f"Продукт {i}", f"Описание {i}",
#                                           f"{i * 100}"))

# for i in range (5, 9):
#     cursor.execute("DELETE FROM Products WHERE id = ?", (f"{i}",))

def get_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")

    rows = cursor.fetchmany(4)
    titles = []
    for title in rows:
        titles.append(title[1])

    descriptions = []
    for description in rows:
        descriptions.append(description[2])

    prices = []
    for price in rows:
        prices.append(price[3])

    return titles, descriptions, prices

get_all_products()

# a = cursor.execute("SELECT * FROM Products")
# total2 = cursor.fetchall()
# print(total2[0] [0])


connection.commit()
connection.close()