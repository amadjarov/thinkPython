import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', '1', 'hangman')

cur = con.cursor()
with con:
    cur.execute("INSERT INTO player(player_name) VALUES('Big Mich')")