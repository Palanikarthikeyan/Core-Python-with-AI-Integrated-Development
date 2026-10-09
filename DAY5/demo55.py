import sqlite3

try:
    conn = sqlite3.connect("C:\\users\\karth\\prod.db")
except Exception as eobj:
    print("DB Connection failed."+str(eobj))

sth = conn.cursor()
sth.execute("select *from prod")
for var in sth:
    print(var)
conn.close()