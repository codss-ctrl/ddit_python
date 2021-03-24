import requests 
from bs4 import BeautifulSoup

URL = 'http://192.168.41.3:7070/HELLOWEB/tel_list.jsp' 
response = requests.get(URL) 
html = response.text
soup = BeautifulSoup(html, 'html.parser')

tds = soup.find_all("td")

for i in tds:
    print(i.text)



