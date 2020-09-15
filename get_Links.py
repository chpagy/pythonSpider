import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

index_page_num=list(range(1,1291))
print ("页面序列生成成功！"+time.strftime("%Y-%m-%d %H:%M:%S"))
index_page_list=[]
for x in index_page_num:
	index_page_list.append("http://www.langji520.com/lianai/index_"+str(x)+".html")
print ("index_page_list生成成功！"+time.strftime("%Y-%m-%d %H:%M:%S"))
content_page_list=[]
print ("初始化index_page_list生成成功！"+time.strftime("%Y-%m-%d %H:%M:%S"))
for idx in index_page_list:
	html=urlopen(idx)
	bsObj=BeautifulSoup(html,"html.parser")
	print("初始化对象"+idx+"成功！"+time.strftime("%Y-%m-%d %H:%M:%S"))
	for k in bsObj.find_all('a',attrs={'href':re.compile('html'),}):
		content_page_list.append(k.get('href'))
		print("更新内容列表"+k.get('href')+"成功！"+time.strftime("%Y-%m-%d %H:%M:%S"))
print ("解析内容网页成功！"+time.strftime("%Y-%m-%d %H:%M:%S"))		
for con in content_page_list:
	filename='content_page_list.txt'
	with open(filename,'a') as f:
		f.write(con)
		f.write("\n")#将列表内容输出到文件
		print("更新内容列表"+con+"成功！"+time.strftime("%Y-%m-%d %H:%M:%S"))
print ("txt文件生成成功！"+time.strftime("%Y-%m-%d %H:%M:%S"))
