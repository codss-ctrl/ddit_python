import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()
sql = "insert into sample (col01,col02,col03) values (:1,:2,:3)"
cs.execute(sql,('9','5','5'))
print(cs.rowcount)

cs.close()
conn.commit()
conn.close()