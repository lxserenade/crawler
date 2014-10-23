#!/use/bin/env python
#-*- coding:utf8 -*-
import os,sys
import urllib
import re
import json
import csv
import time





#e.x  time_flag='2014-10-22 00:00:00'
def is_new_page(url,time_target):
	tf=int(time.mktime(time.strptime(time_flag, "%Y-%m-%d %H:%M:%S")))
	page=urllib.urlopen(url)
	page_mtime=" ".join(page.info()["Last-Modified"].split(' ')[1:-1])
	pt=time.mktime(time.strptime(page_mtime,"%d %b %Y %H:%M:%S"))
	return pt>=tf 


time_flag='2014-10-22 00:00:00'
url='http://news.sina.com.cn/c/2014-10-18/014031007028.shtml'
print is_new_page(url,time_flag)