import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()
sql = "update sample set col02=:1,col03=:2 where col01=:3"
cs.execute(sql,('1','1','5'))
print(cs.rowcount)

cs.close()
conn.commit()
conn.close()