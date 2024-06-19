import sqlite3 as sq

db = sq.connect("C:/Users/User/PycharmProjects/pythonProject5/person2.db")
cur = db.cursor()




async def get_photo(name):
    return cur.execute(f"SELECT id FROM images where name == '{name}'").fetchone()[0]

