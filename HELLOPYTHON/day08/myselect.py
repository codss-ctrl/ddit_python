import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()
rs = cs.execute('select col01,col02,col03 FROM sample')

for record in rs:
    print(record[1])

cs.close()
conn.close()