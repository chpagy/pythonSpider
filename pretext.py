import shutil
import re
import time

readPath='content_page_list.txt'
writePath='content_page_list_tichong.txt'
lines_seen=set()
outfiile=open(writePath,'a+',encoding='utf-8')
f=open(readPath,'r',encoding='utf-8')
for line in f:
    if line not in lines_seen:
        outfiile.write(line)
        lines_seen.add(line)

lineList=[]
matchPattern1 = re.compile(r'index')
matchPattern2 = re.compile(r'sitemap')
file=open('content_page_list_tichong.txt','r',encoding='UTF-8')
while 1:
    line=file.readline()
    if not line:
        print("读取文件出错！")
        break
    elif matchPattern1.search(line):
        pass
    else:
        lineList.append(line)
file.close()

file=open(r'content_page_list_tichong_tichu.txt','w',encoding='UTF-8')
for i in lineList:
    file.write(i)
    print(i)
file.close()

