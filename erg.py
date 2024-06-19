import sqlite3 as sq

db = sq.connect("C:/Users/User/PycharmProjects/pythonProject5/person2.db")
cur = db.cursor()

name = "robot3"
id = "AgACAgIAAxkBAAIItGZyeLPaQcbrkwKsFqy2Loj-GQndAAKl3jEbs-KQSzEJF7GZMB0XAQADAgADeQADNQQ"

cur.execute("CREATE TABLE IF NOT EXISTS images(name TEXT PRIMARY KEY,id TEXT)")
db.commit()


cur.execute("INSERT INTO images VALUES(?, ?)", (name, id))
db.commit()



