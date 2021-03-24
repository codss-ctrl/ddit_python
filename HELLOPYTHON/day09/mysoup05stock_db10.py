import requests 
from bs4 import BeautifulSoup
import cx_Oracle
import datetime
import time

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()
sql = "insert into stock (S_CODE,S_NAME,CPRICE,IN_TIME) values (:1,:2,:3,:4)"

URL = 'https://vip.mk.co.kr/newSt/rate/item_all.php' 

for k in range(10):

    response = requests.get(URL) 
    response.encoding = "euc-kr"
    
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
     
    tds = soup.select('.st2')
    
    in_time = datetime.datetime.now().strftime("%Y%m%d.%H%M") 
    for i in tds:
        s_name = i.text
        s_code = i.find("a")['title']
        cprice = i.parent.find_all("td")[1].text.replace(",","")
        cs.execute(sql,(s_code,s_name,cprice,in_time))
        
        print(s_name,s_code,cprice)
    
    
    
    conn.commit()
    time.sleep(60)
    

cs.close()
conn.close()

