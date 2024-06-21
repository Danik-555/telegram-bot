import sqlite3 as sq

db = sq.connect("person2.db")
cur = db.cursor()

name = "frog"
id = "AgACAgIAAxkBAAILRmZ1JBusowAB5BIDd3hsWbZUlc_r5AACmtUxG97-qEu7ep3gPTQNugEAAwIAA3MAAzUE"
cur.execute("CREATE TABLE IF NOT EXISTS images(name TEXT PRIMARY KEY,id TEXT)")
db.commit()


cur.execute("INSERT INTO images VALUES(?, ?)", (name, id))
db.commit()



