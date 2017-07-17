# -*- coding: utf-8 -*-
import requests
import re
import os
import sys

reload(sys)                     
sys.setdefaultencoding('utf-8') 
dirpath = r'/Users/tracy.liu/Desktop/python_work/picture2'
if not os.path.isdir(dirpath):
    os.mkdir(dirpath)

url = r"http://bbs.51meishu.com/forum.php?mod=forumdisplay&fid=88"
html = requests.get(url, timeout = 15).text
urls = re.findall(r'a href="(.*?extra=page%3D1)"',html)

index = 1
for pic_url in urls:
	#  print pic_url
	pic_url = pic_url.replace('amp;','')
	inter_html = requests.get(pic_url).text
	inter_urls = re.findall(r'var _pic = encodeURI\((.*?)\)', inter_html)
	inter_pic_urls = re.split(r'[\'\|]', str(inter_urls))
	#print inter_pic_urls
	if len(inter_pic_urls) > 1:
		del inter_pic_urls[0]
		del inter_pic_urls[-1]
	else:
		continue
	
	for pic in inter_pic_urls:
	    #print pic
	    try:
	        res = requests.get(pic, timeout = 15)
	        if res.status_code != requests.codes.ok:
	            print res.status_code+":"+pic
	            continue
	    except Exception as e:
	        print "抛出异常"+":"+pic

	    filename = os.path.join(dirpath,str(index)+".jpg")
	    with open(filename,"wb") as f:
	        f.write(res.content)
	        index += 1
	        print index







