#-*-coding:utf-8-*-
from matplotlib import pyplot as plt

f = open('video_data.txt', 'r')

lines = f.readlines()
data = []
for line in lines:
	li = eval(line)
	for item in li:
		data.append(item)
	break

print len(data)

a1 = [x[0] for x in data if x[0]]
a2 = [int(x[1].replace(',', '')) for x in data if x[0]]
plt.plot(a1, a2, 'ro')
plt.show()