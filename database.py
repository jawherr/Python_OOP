import sqlite3

con = sqlite3.connect('data.db')

c = con.cursor()

#c.execute('CREATE TABLE IF NOT EXISTS names(fname TEXT ,lname TEXT ,age INT,salary REAL)')

#c.execute('INSERT INTO names VALUES("Ahmed" ,"Essa" ,27, 3000) ,("Usama" ,"Essa" ,22, 6000)')
#con.commit()

c.execute('SELECT * FROM names')
for row in c.fetchall():
    print(row)
con.close()
