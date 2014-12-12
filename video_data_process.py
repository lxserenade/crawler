#-*-coding:utf-8-*-
from matplotlib import pyplot as plt
import MySQLdb
import datetime, calendar ,time
import math


date='20141001'
conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='sina',charset="utf8")
cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
sql = "SELECT view,comments FROM sina_top_video WHERE date="+date;
cursor.execute(sql)

data=cursor.fetchall()
views=[item['view'] for item in data if item['comments']]
comments=[item['comments'] for item in data if item['comments']]

print len(views)
print len(comments)
score=[]


for i in range(0, len(views)):
	#print 0.3+math.log10(10+views[i])/math.log10(10+max(views)))+(0.7+math.log10(10+comments[i])/math.log10(10+max(comments))
	score.append(0.3*(math.log10(10+views[i])/math.log10(10+max(views)))+0.7*(math.log10(10+comments[i])/math.log10(10+max(comments))))

print score.sort(reverse=True)
plt.title(date)
plt.xlabel('content')
plt.ylabel('score')
plt.plot(score,'ro')
plt.show()


# lines = f.readlines()
# data = []
# for line in lines:
# 	li = eval(line)
# 	for item in li:
# 		data.append(item)
# 	break

# print len(data)

# a1 = [x[0] for x in data if x[0]]
# a2 = [int(x[1].replace(',', '')) for x in data if x[0]]
# plt.plot(a1, a2, 'ro')
# plt.show()