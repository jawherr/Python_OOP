import sqlite3

con = sqlite3.connect('data.db')

c = con.cursor()


#c.execute('UPDATE names SET fname="Ali" ,lname="Omer" ,salary=1000 WHERE age=33')
c.execute('DELETE FROM names WHERE fname="Usama"')
print('Done')
con.commit()
con.close()
