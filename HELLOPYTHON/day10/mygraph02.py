import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D 
import numpy as np
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



fig = plt.figure()
ax = fig.gca(projection='3d')  

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')

s_names = ["삼성전자","LG","SK","SK","SK"]

cnt = len(getCprice("삼성전자"))
y = range(cnt)
x = np.zeros(cnt)

for i,s_name in enumerate(s_names):
    z = getCprice(s_name)
    ax.plot(x+i, y, z) 

# z = getCprice(s_names[0])
# ax.plot(x+0, y, z)  
# 
# z = getCprice(s_names[1])
# ax.plot(x+1, y, z)  
# 
# z = getCprice(s_names[2])
# ax.plot(x+2, y, z)  



plt.show()





