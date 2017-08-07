#get city

import requests
import re
from insert_city import insert


data = requests.get("http://www.cnblogs.com/xmyy/archive/2012/05/29/2523536.html")

regex = r'101\d{6}[\x00-\xff][\u4e00-\u9fa5]+'
pattern = re.compile(regex)
ma = re.findall(pattern,data.text)

#with open('city.txt','w') as f:
#	for city in ma:
#		citys = city.split('=')
#		f.write(citys[0]+','+citys[1]+'\r\n')


for city in ma:
	citys = city.split('=')
	insert(citys[0],citys[1])


if(200!=data.status_code):
	print('请求状态有问题，状态码为：'+data.status_code)
else:
	html = data.text





