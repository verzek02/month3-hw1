import sqlite3
from pathlib import Path


# СУБД
# sqlite
# MySQL, Postgres, MariaDB

def init_db():
    """Для создания соединения с sqlite БД"""
    # DOCSTRING
    global db, cursor
    DB_NAME = 'db.sqlite'  # .sqlite, .db
    DB_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(DB_PATH / DB_NAME)
    cursor = db.cursor()


def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS survey(
        survey_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        stack TEXT,
        languages TEXT,
        time FLOAT
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        photo TEXT
    )""")
    db.commit()


def delete_products():
    cursor.execute("""DROP TABLE IF EXISTS products""")
    db.commit()


def insert_products():
    cursor.execute("""INSERT INTO products(name, price, photo)
        VALUES ('Самые лучшие часы', 200, 'images/самые лучшие часы.jpeg'),
        ('Самые дорогие часы', 400, 'images/самые дорогие часы.jpg')
    """)
    db.commit()


def get_products():
    init_db()
    cursor.execute("""SELECT * FROM products""")
    return cursor.fetchall()


def insert_survey(data):
    init_db()
    cursor.execute("""
    INSERT INTO survey(name, age, gender, stack, languages, time)
        VALUES (:name, :age, :gender, :stack, :languages, :time)

    """, {
        'name': data['name'],
        'age': data['age'],
        'gender': data['gender'],
        'stack': data['stack'],
        'languages': data['languages'],
        'time': data['time'],
    })
    db.commit()


def create_table_cars():
    init_db()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dictionary (
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        price TEXT,
        description TEXT,
        link TEXT UNIQUE
    )
    """)
    db.commit()


# Вставка данных
def pop_cars(data1):
    init_db()
    for item in data1:
        cursor.execute("""
        INSERT OR IGNORE INTO dictionary (name, price, description, link)
        VALUES (?, ?, ?, ?)
        """, (item["name"], item["price"], item["descr"], item["link"]))

    db.commit()


def get_data():
    init_db()
    cursor.execute(
        '''
        SELECT * FROM dictionary
        '''
    )
    return cursor.fetchall()

if __name__ == "__main__":
    init_db()
    create_tables()
    # insert_products()
    create_table_cars()


