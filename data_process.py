#!/use/bin/env python
#-*- coding:utf8 -*-
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



# f=open('./log.txt','r')
# af=open('./1025-1027.txt','w')
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


def plot_data(l):
	fig, ax = plt.subplots()
	counts, bins, patches = ax.hist(l,30,facecolor='yellow', edgecolor='gray')

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
	    ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
	        xytext=(0, -50), textcoords='offset points', va='top', ha='center')


	# Give ourselves some more room at the bottom of the plot
	plt.subplots_adjust(bottom=0.15)
	plt.grid(True)
	plt.xlabel("total reply")
	plt.ylabel("pages")
	plt.title("2014/10/21-2014/10/22  sina new pages")
	plt.show()


f=open('./1025-1027.txt','r')
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

plot_data(total_list)

