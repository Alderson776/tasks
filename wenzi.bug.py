import requests
from bs4 import beautifulsoup
import os
if not os.path.exists('./wenzi,text')
    os.mkdir('./wenzi.text')
url = 'https://itawenya.cn/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
requests.get( url = url,headers= headers).text
beautifulsoup(page_text,'lxml')
li_list = soup.slect('.slide>ul>li')
open('./wenzi.text','w',encoding='utf-8') as fp:
fp.write(page_text)

print(page_text,'successfully')
