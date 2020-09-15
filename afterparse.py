import re
import os
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

f = open(r'content_page_list_tichong_tichu.txt','r')
a = []
for i in f.readlines():
	lst=i.strip('\n')
	a.append(lst) 
f.close()

for x1 in a:
	try:
		html=urlopen("http://www.langji520.com"+x1)
		ctObj=BeautifulSoup(html,"html.parser")
		ctObj.encoding='utf-8'
		content=ctObj.find(name='div',attrs={'class':"article_con"}).find("p").get_text()
		print(content)
		fo=open("langji520.txt","a")
		fo.write(content+'\r\n')
		print("write Successful!"+str(x1)+"Still remaining:"+str(len(a)-a.index(x1)))
	except AttributeError as reason:
		print("AttributeError:"+str(reason)+str(x1))
		pass
	except UnicodeEncodeError as reason:
		print(str(reason)+str(x1))
		pass
	finally:
		f.close()
		
