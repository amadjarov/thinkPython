import MySQLdb as mdb
a ="ajsd"
b="aksjd"
c=1
con = mdb.connect('localhost', 'testuser', '1', 'hangman')
cur = con.cursor()
with con:
    cur.execute("insert into game(rightGuess,wrongGuess,result) values ('%s','%s','1');"%(a,b))
    cur.execute("select player_id from player where player_name = 'gogo';")
i = cur.fetchone()[0]
print i