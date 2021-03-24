import requests
import json

url = "https://dapi.kakao.com/v2/search/image"
queryString = {"query":"남주혁"}
header = {'authorization':'KakaoAK 3dd8c108e91c93e0cf17d78e46c2d1c1'}
r = requests.get(url, headers=header, params=queryString)

myjson = json.loads(r.text)
# print(myjson)

for i in myjson['documents']:
    print(i['collection'],end="\t")
    print(i['datetime'],end="\t")
    print(i['display_sitename'],end="\t")
    print(i['doc_url'],end="\t")
    
    print(i['height'],end="\t")
    print(i['image_url'],end="\t")
    print(i['thumbnail_url'],end="\t")
    print(i['width'])

    
    