import cx_Oracle

def getCprice(s_name):
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')
    cs = conn.cursor()
    rs = cs.execute("select cprice FROM stock where s_name='"+s_name+"' order by in_time")
    
    ret = []
    for record in rs:
        ret.append(record[0])
    
    cs.close()
    conn.close()
    return ret
    
arr = getCprice("삼성전자")
print(arr)