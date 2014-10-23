#!/use/bin/env python
#-*- coding:utf8 -*-
import os,sys
import urllib
import re
import json
import csv
import time
import matplotlib

# f=open('./1021-1022.txt','r')
# af=open('./1021-1022_new.txt','w')
# data=f.readlines()

# for line in data:
# 	if line[0]=='\n':
# 		continue
# 	if line[0]=='{' and line[1]=='{':
# 		line=line[1:-2]
# 	if not eval(line)['show']:
# 		continue
# 	af.write(line)
# 	af.write('\n')
# f.close()
# af.close()


f=open('./1021-1022_new.txt','r')
data=f.readlines()

qreply_list=[]
total_list=[]
show_list=[]
for line in data:
	if not line=='\n':
		qreply_list.append(eval(line)['qreply'])
		total_list.append(eval(line)['total'])
		show_list.append(eval(line)['show'])

print len(qreply_list)
print len(total_list)
print len(show_list)




