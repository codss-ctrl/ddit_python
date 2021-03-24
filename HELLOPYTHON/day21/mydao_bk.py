import cx_Oracle

def getData():
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor()
    rs = cs.execute('select col01,col02,col03 FROM sample')

    list = []

    for record in rs:
        list.append({'col01':record[0],'col02':record[1],'col03':record[2]})

    cs.close()
    conn.close()
    
    return list
    
def myinsert(col01,col02,col03):
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor()
    sql = "insert into sample (col01,col02,col03) values (:1,:2,:3)"
    cs.execute(sql,(col01,col02,col03))
    cnt = cs.rowcount
    
    cs.close()
    conn.commit()
    conn.close()    
    return cnt
    
    
def myupdate(col01,col02,col03):
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor()
    sql = "update sample set col02=:1,col03=:2 where col01=:3"
    cs.execute(sql,(col02,col03,col01))
    cnt = cs.rowcount
    
    cs.close()
    conn.commit()
    conn.close()    
    return cnt    

def mydelete(col01):
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor()
    sql = "delete from sample where col01 = :1"
    cs.execute(sql,(col01,))
    cnt = cs.rowcount
    
    cs.close()
    conn.commit()
    conn.close()    
    return cnt  
    
# list = getData()
# print(list)

# cnt = myinsert(6, 6, 6)
# print(cnt)

# cnt = myupdate(6, 5, 5)
# print(cnt)

cnt = mydelete(6)
print(cnt)

    