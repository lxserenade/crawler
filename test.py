#!/use/bin/env python
#-*- coding:utf8 -*-
import os,sys
import urllib
import urllib2
import re
from HTMLParser import HTMLParser

from bs4 import BeautifulSoup
# path=os.getcwd()+"\\"
# filename="test.shtml"
# f=open(path+filename,"r")
# soup = BeautifulSoup(f)

# url='http://news.sina.com.cn/c/2014-10-18/014031007028.shtml'

# data=urllib.urlopen(url).read().decode('gb2312','ignore')

# soup=BeautifulSoup(data)
# print data




def processurl(url):
	global num
	num=num+1
	data=urllib.urlopen(url).read().decode('gb2312','ignore')
	#print data

#=================================================
# 递归遍历指定的目录  
# path-遍历起始绝对路径  


TargetFileType=['html','shtml']
num=0
def listyoudir(path):  
	global num
	for i in os.listdir(path):
		if not os.path.isdir(path + '\\' + i):
			if i.split('.')[-1].lower() in TargetFileType:
				url='http:/'+(path + '\\' + i)[8:].replace('\\','/')
				processurl(url)
		else:
			listyoudir(path + '\\'+i)

#测试代码  
rootpath = os.path.abspath('.')  
listyoudir(rootpath)
print num