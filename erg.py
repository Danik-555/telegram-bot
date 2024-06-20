import sqlite3 as sq

db = sq.connect("C:/Users/User/PycharmProjects/pythonProject5/person2.db")
cur = db.cursor()

name = "stars3"
id = "AgACAgIAAxkBAAIJFWZz1wOLpRGIzjjdpnhq5e1vwwjBAALs3zEb2R6hSyZkojlOb1HIAQADAgADcwADNQQ"

cur.execute("CREATE TABLE IF NOT EXISTS images(name TEXT PRIMARY KEY,id TEXT)")
db.commit()


cur.execute("INSERT INTO images VALUES(?, ?)", (name, id))
db.commit()



