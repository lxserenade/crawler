#!/use/bin/env python
#-*- coding:utf8 -*-
import os,sys
import urllib
import re
import json
import csv

########################
#return {{u'qreply': int, u'total': int, u'show': int}}
# total:参与人数（评论＋点赞or支持＋回复数），show：评论数 qreply：回复数
def get_news_comment(url):
    #html data
	data=urllib.urlopen(url).read().decode('gb2312','ignore')

	try:
		#get channel,newsid
		channel_pattern = re.compile(r'channel:\'(.*?)\',')
		channel = channel_pattern.search(data).group(1)
		newsid_pattern = re.compile(r'newsid:\'(.*?)\',')
		newsid = newsid_pattern.search(data).group(1)
	except:
		return '{can not find channel or newsid}'
	#get comment count from json_data
	comment_url='http://comment5.news.sina.com.cn/page/info?format=js&channel='+channel+'&newsid='+newsid
	comment_data=urllib.urlopen(comment_url).read().decode('gb2312','ignore')
	comment=json.loads(comment_data[9:])
	return comment["result"]["count"]
#########################


#########################
# 递归遍历指定的目录  
# path-遍历起始绝对路径  
TargetFileType=['html','shtml']
log=[]
num=0
def process(path):  
	global num
	for i in os.listdir(path):
		if not os.path.isdir(path + '\\' + i):
			if i.split('.')[-1].lower() in TargetFileType:
				url='http:/'+(path + '\\' + i)[8:].replace('\\','/')
				log.addpend(get_news_comment(url))
		else:
			listyoudir(path + '\\'+i)



#测试代码  
rootpath = os.path.abspath('.')  
process(rootpath)
print log