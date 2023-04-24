import sqlite3
from pathlib import Path


DB_NAME = 'db.sqlite3'
DB_PATH = Path(__file__).parent.parent
# СУБД - Система управления базами данных
db = sqlite3.connect(DB_PATH / DB_NAME)
cursor = db.cursor()



def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS survey(
        survey_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        user_id INTEGER,
        time DATETIME
    )""")
    db.commit()


# def insert_survey(state):
#     cursor.execute("""
#     INSERT INTO survey(name, age, gender, user_id)
#         VALUES (:name, :age, :gender, :user_id),
#
#     """, {
#         'name': get('name'),
#         'age': data.get('age'),
#         'gender': gender,
#         'user_id': user_id
#     })
#     db.commit()

# d
# )

if __name__ == "__main__":
    init_db()
    create_tables()
    insert_survey()
