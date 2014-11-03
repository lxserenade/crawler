#!/use/bin/env python
#-*- coding:utf8 -*-

######################
#this script finds the number of comments 
# of the most top page view amoung sinanews (http://news.sina.com.cn/hotnews/)  
# and plot  hist
######################

import os,sys
import urllib
import re
import json
import csv
import time
import matplotlib
from collections import Counter
from  matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import socket


socket.setdefaulttimeout(10) # 10 秒钟后超时


def plot_data(l):
	fig, ax = plt.subplots()
	counts, bins, patches = ax.hist(l,50,facecolor='yellow', edgecolor='gray')

	# Set the ticks to be at the edges of the bins.
	#ax.set_xticks(bins)
	# Set the xaxis's tick labels to be formatted with 1 decimal place...
	#ax.xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))

	
	# Label the raw counts and the percentages below the x-axis...
	bin_centers = 0.5 * np.diff(bins) + bins[:-1]
	for count, x in zip(counts, bin_centers):
	    # Label the raw counts
	    ax.annotate(str(int(count)), xy=(x, 0), xycoords=('data', 'axes fraction'),
	        xytext=(0, -40), textcoords='offset points', va='top', ha='center')

	    # Label the percentages
	    percent = '%0.0f%%' % (100 * float(count) / counts.sum())
	    #ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),xytext=(0, -50), textcoords='offset points', va='top', ha='center')


	# Give ourselves some more room at the bottom of the plot
	plt.subplots_adjust(bottom=0.15)
	plt.grid(True)
	plt.xlabel("total reply")
	plt.ylabel("pages")
	plt.title(time.strftime('%Y-%m-%d',time.localtime(time.time()))+"top_news@sina")
	plt.show()


def getTopClick(num):
	url='http://top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=www_all&top_time=20141031&top_show_num='+str(num)+'&top_order=ASC&js_var=all_1_data01'
	data=(urllib.urlopen(url).read().decode('gb2312','ignore')[18:-2])
	return json.loads(data)

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
    	return "{u'qreply': None, u'total': None, u'show': None}"
    return comment["result"]["count"]
#########################

t=[]
tc=getTopClick(10000)
for item in tc["data"]:
	tmp=(get_news_comment(item["url"]))
	print tmp
	t.append(str(tmp))
	print item["url"]


qreply_list=[]
total_list=[]
show_list=[]
# print t


for line in t:
	if not line[0]=='{' :
		continue	
	if not eval(line)['show']:
		continue
	qreply_list.append(eval(line)['qreply'])
	total_list.append(eval(line)['total'])
	show_list.append(eval(line)['show'])


print len(qreply_list)
print len(total_list)
print len(show_list)

plot_data(total_list)
