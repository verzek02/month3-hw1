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
        user_id INTEGER
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
        VALUES ('Самая лучшая книга', 200, 'images/cat.webp'),
        ('Самая интересная книга', 400, 'images/cat.webp')
    """)
    db.commit()


def get_products():
    data = cursor.execute("""SELECT * FROM products""")
    return data.fetchall()


def insert_survey(data, gender, user_id):
    # cursor.execute("""
    # INSERT INTO survey(name, age, gender, user_id)
    #     VALUES ("Daniel", 19, "male", 12312),
    #     ("Igor", 30, "male", 232323)
    # """)
    cursor.execute("""
    INSERT INTO survey(name, age, gender, user_id)
        VALUES (:name, :age, :gender, :user_id),

    """, {
        'name': data.get('name'),
        'age': data.get('age'),
        'gender': gender,
        'user_id': user_id
    })
    db.commit()

# if __name__ == "__main__":
#     print(init_db.__doc__)
#     init_db()
#     create_tables()
#     insert_survey()