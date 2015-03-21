#!/use/bin/env python
#-*- coding:utf8 -*-

import urllib
import re
import json
import time,datetime
import numpy as np
from my_leastsq import *
seed=137516224
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


##由于接口限制，为避免参数过长，每次抓取100个，多次抓取
for i in range(100):
	for j in range(100):
		vids.append(str(seed+j)+'-'+str(seed+j))
	url=getCount_url+'x'.join(vids)
	data=urllib.urlopen(url).read()
	data=eval(data[6:-2])
	for (key,value) in data.items():
		count_data.append(int(str(value).replace(',','')))

	seed=seed+j
	vids=[]


count_data=sorted(count_data,reverse=True)
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
