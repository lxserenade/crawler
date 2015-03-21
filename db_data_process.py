#!/use/bin/env python
#-*- coding:utf8 -*-

#########
#function: plot hist of views/comments. 
#data base:mysql,
#usage:--

import json
from  matplotlib import pyplot as plt
import numpy as np
import MySQLdb
import datetime, calendar ,time
from matplotlib.pylab import figure, show
from my_leastsq import *
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
	plt.title("2014-1-1 sina video views ")
	plt.show()



d1 = datetime.datetime(2014, 3, 1)

for i in range(7):
	d=d1 + datetime.timedelta(1)
	date=d.strftime('%Y-%m-%d')
	d1=d
	print date
	conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='sina',charset="utf8")
	cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

	sql="select view,comments from sina_top_video where date=\""+str(date)+"\" and comments!=\"NULL\""
	cursor.execute(sql)
	data=cursor.fetchall()
	cursor.close()
	conn.commit()
	conn.close()

	view=[]
	comments=[]
	# print data
	for item in data:
		view.append(item["view"])
		comments.append(item["comments"])
	sorted(view)
	index=[i for i in range(1,len(view)+1)]
	# print view
	test_x=np.array(view)
	# print test_x
	leastsq_plot(test_x,date)

# fig=figure()
# im1 = fig.add_subplot(2,1,1)
# im2=fig.add_subplot(2,1,2)
# im1.scatter(index,view)
# im2.loglog(index,view)

# im1.set_xlabel("index")
# im1.set_ylabel("popular degree")
# im1.set_title("normal")
# im2.set_title("log-log")
# im2.set_xlabel("index")
# im2.set_ylabel("popular degree")

# plt.loglog(index,view,"o")
# plt.xlabel("index")
# plt.ylabel("popular degree")
# plt.title("log-log")
# plt.xlim(0,100)
# plt.grid(True)
# plt.show()

# plot_data(view)
#print data[0]
