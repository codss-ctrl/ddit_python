import cx_Oracle
import datetime

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()
sql = "insert into stock (S_CODE,S_NAME,CPRICE,IN_TIME) values (:1,:2,:3,:4)"
in_time = datetime.datetime.now().strftime("%Y%m%d.%H%M")


cs.execute(sql,('9','5','5',in_time))

conn.commit()
cs.close()
conn.close()