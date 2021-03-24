import requests 
URL = 'http://192.168.41.3:7070/HELLOWEB/tel_list.jsp' 
response = requests.get(URL) 
print(response.status_code)
print(response.text)

