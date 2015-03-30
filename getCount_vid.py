#!/use/bin/env python
#-*- coding:utf8 -*-

import urllib
import re
import json
import time,datetime
import numpy as np
from my_leastsq import *
seeds=[137562793,137565791,137577708,137565321,137580358]
seed=137565321
vids=[]
count_data=[]
getCount_url="http://count.video.sina.com.cn/getCount.php?vids="




# ##逐一抓取
# for i in range(1000):
# 	print i
# 	try:
# 		vid=str(seed+i)+'-'+str(seed+i)
# 		url=getCount_url+vid
# 		data=urllib.urlopen(url).read()
# 		data=eval(data[6:-2])
# 		count_data.append(int(str(data.items()[0][1]).replace(',','')))
# 	except:
# 		print 'error:',i
# 		continue

# count_data=sorted(count_data,reverse=True)
# print len(count_data)
# print count_data

# #################
# seeds
# for seed in seeds:
# 	for j in range(20):
# 		vids.append(str(seed+j)+'-'+str(seed+j))
# 	url=getCount_url+'x'.join(vids)
# 	print url
# 	data=urllib.urlopen(url).read()
# 	data=eval(data[6:-2])
# 	for (key,value) in data.items():
# 		count_data.append(int(str(value).replace(',','')))

# 	seed=seed+j

# ######################

##由于接口限制，为避免参数过长，每次抓取100个，多次抓取
# for i in range(10):
# 	for j in range(100):
# 		vids.append(str(seed+j)+'-'+str(seed+j))
# 	url=getCount_url+'x'.join(vids)
# 	data=urllib.urlopen(url).read()
# 	data=eval(data[6:-2])
# 	for (key,value) in data.items():
# 		count_data.append(int(str(value).replace(',','')))

# 	seed=seed+j
# 	vids=[]

###
#from exist data
count_data=[573674, 442602, 412795, 204423, 168829, 164491, 159310, 158141, 157096, 153180, 145081, 139434, 129300, 119760, 119179, 118646, 118277, 112062, 111447, 110206, 108115, 106262, 105100, 104506, 99258, 94363, 89344, 88772, 88349, 83624, 83421, 82624, 81436, 79558, 79226, 76306, 75596, 73926, 72245, 71814, 70909, 67419, 63735, 62951, 61201, 58682, 56406, 55591, 54305, 52628, 52312, 52303, 52186, 51948, 51240, 51062, 49610, 47474, 45783, 45070, 44821, 44392, 44081, 43909, 43824, 43819, 42543, 42316, 41991, 41207, 41010, 40837, 39569, 38667, 38631, 38461, 37392, 36767, 36746, 34454, 34135, 33987, 31796, 31457, 31131, 30516, 30460, 30328, 30304, 29834, 28232, 28124, 28123, 28032, 27576, 27395, 27353, 26829, 26476, 25940, 25893, 25728, 25230, 24746, 24625, 24597]
####


count_data=sorted(count_data,reverse=True)
count_data=count_data[0:100]
print len(count_data)
print count_data


#获得当前时间
now = datetime.datetime.now()
#转换为指定的格式:
otherStyleTime = now.strftime("%Y-%m-%d %H:%M")

f=open("video_data.txt",'a')
f.write(otherStyleTime+"\n"+str(count_data)+"\n\n")
f.close()
leastsq_plot(np.array(count_data),otherStyleTime)
