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




##逐一抓取
for i in range(1000):
	print i
	try:
		vid=str(seed+i)+'-'+str(seed+i)
		url=getCount_url+vid
		data=urllib.urlopen(url).read()
		data=eval(data[6:-2])
		count_data.append(int(str(data.items()[0][1]).replace(',','')))
		vids.append(vid)
	except:
		print 'error:',i
		continue
print vid


# ##由vids一次抓取
# for i in range(200):
# 	vids.append(str(seed+i)+'-'+str(seed+i))

# url=getCount_url+'x'.join(vids)
# data=urllib.urlopen(url).read()
# data=eval(data[6:-2])
# for (key,value) in data.items():
# 	count_data.append(int(str(value).replace(',','')))


