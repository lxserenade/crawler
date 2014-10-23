#!/use/bin/env python
#-*- coding:utf8 -*-
import os,sys
import urllib
import re
import json
import csv
import socket
import time

socket.setdefaulttimeout(10) # 10 秒钟后超时
########################
#return {{u'qreply': int, u'total': int, u'show': int}}
# total:参与人数（评论＋点赞or支持＋回复数），show：评论数 qreply：回复数
def get_news_comment(url):
    try:
		#html data
		data=urllib.urlopen(url).read().decode('gb2312','ignore')
		#get channel,newsid
		channel_pattern = re.compile(r'channel:\'(.*?)\',')
		channel = channel_pattern.search(data).group(1)
		newsid_pattern = re.compile(r'newsid:\'(.*?)\',')
		newsid = newsid_pattern.search(data).group(1)
		#get comment count from json_data
		comment_url='http://comment5.news.sina.com.cn/page/info?format=js&channel='+channel+'&newsid='+newsid
		comment_data=urllib.urlopen(comment_url).read().decode('gb2312','ignore')
		comment=json.loads(comment_data[9:])
		com=comment["result"]["count"]
    except Exception, e:
    	print e
    	return "{{u'qreply': None, u'total': None, u'show': None}}"
    return comment["result"]["count"]
#########################


#########################
#if the file was created(modified) after time_flag, return true;
#e.x  time_flag='2014-10-22 00:00:00'
def is_new_file(filePath,time_flag):
    tf=int(time.mktime(time.strptime(time_flag, "%Y-%m-%d %H:%M:%S")))
    mt=os.stat(filePath).st_mtime#file modify time
    return mt>=tf

#########################
#if the page was modified after time_flag, return true;
#e.x  time_flag='2014-10-22 00:00:00'
def is_new_page(url,time_target):
	try:
		tf=int(time.mktime(time.strptime(time_flag, "%Y-%m-%d %H:%M:%S")))
		page=urllib.urlopen(url)
		page_mtime=" ".join(page.info()["Last-Modified"].split(' ')[1:-1])
		pt=time.mktime(time.strptime(page_mtime,"%d %b %Y %H:%M:%S"))
	except Exception,e:
		print "get last-modified time error"
		return False
	return pt>=tf 



##############################################################################


num=0
time_flag='2014-10-23 00:00:00'
#########################
# 递归遍历指定的目录  
# path-遍历起始绝对路径  
TargetFileType=['html','shtml']
log=[]
def process(path):  
	for i in os.listdir(path):
		if not os.path.isdir(path + '\\' + i):	
			if i.split('.')[-1].lower() in TargetFileType:

				url='http:/'+(path + '\\' + i)[8:].replace('\\','/')
				print url
				if is_new_page(url,time_flag):
					
					com=get_news_comment(url)
					global log
					log.append(com)
					global num
					num=num+1
					if num%20==0:
						print '----------------------------------'
						print num
						print '----------------------------------'
					
		else:
			process(path + '\\'+i)



#测试代码  
rootpath = os.path.abspath('D:\\LX\\li\\')
process(rootpath)
print len(log)

fl=open('log.txt','w')
for i in log:
    fl.write(str(i))
    fl.write("\n")
fl.close()