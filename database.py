import sqlite3 as sq

db = sq.connect('person1.db')
cur = db.cursor()

async def start_db():
    global db, cur
    cur.execute("CREATE TABLE IF NOT EXISTS person(user_id TEXT PRIMARY KEY, name TEXT, age TEXT, mail TEXT)")
    db.commit()

async def create_profile(id):
    user = cur.execute(f"SELECT 1 FROM person where user_id == {id}").fetchone()
    if not user:
        cur.execute("INSERT INTO person VALUES(?, ?, ?, ?)", (id, '', '', ''))

async def edit_profile(user_id,name,age, mail):
    cur.execute(f"UPDATE person SET name = ?, age = ?, mail = ? WHERE user_id == ?",
            (name, age, mail, user_id))
    db.commit()




