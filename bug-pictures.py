import re
import os
import requests
if not os.path.exists('./homepage.pictures'):
 os.mkdir('./homepage.pictures')
url = 'https://itawenya.cn/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}
page_text = requests.get(url=url,headers=headers).text
ex = '<div id="homepage">.*?<img src=(.*?)" alt.*?</div>'
img_src_list = re.findall(ex,page_text,re.S)
for src in img_src_list:
    src = 'https:'+src
img_data = requests.get(url=src,headers=headers).content
img_name = src.split('/')[-1]
imgPath = './homepage.pictures'+img_name
with open(imgPath,'wb') as fp:
     fp.write(img_data)
print(img_name,'下载成功！')
