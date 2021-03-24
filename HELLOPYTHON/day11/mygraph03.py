import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D 
import numpy as np
import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()
    
def getCprice(s_name):
    rs = cs.execute("select cprice FROM stock where s_name='"+s_name+"' order by in_time")  
    ret = []
    for record in rs:
        ret.append(record[0])
    
    return ret

def getSnames():
    rs = cs.execute("select s_name from stock group by S_NAME")
    ret = []
    for record in rs:
        ret.append(record[0])

    return ret



fig = plt.figure()
ax = fig.gca(projection='3d')  

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')

s_names = getSnames()
# s_names = ["삼성전자","LG"]

cnt = len(getCprice("삼성전자"))
y = range(cnt)
x = np.zeros(cnt)

for i,s_name in enumerate(s_names):
    z = getCprice(s_name)
    ax.plot(x+i, y, z) 


plt.show()

cs.close()
conn.close()





