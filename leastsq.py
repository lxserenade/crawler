# -*- coding: utf-8 -*- 
import numpy as np 
from scipy.optimize import leastsq
from matplotlib.pylab import figure, show

import math
# test_x=np.array([4389494L, 3257621L, 2815182L, 2678733L, 2064553L, 2016194L, 1849421L, 1455854L, 1352968L, 1335537L, 1324069L, 1177455L, 1165641L, 1146214L, 1133146L, 1121603L, 1119996L, 1014420L, 999229L, 985051L, 976168L, 972726L, 951084L, 911527L, 909337L, 892977L, 882350L, 869869L, 866387L, 862589L, 861686L, 845796L, 838309L, 815209L, 812582L, 803185L, 794341L, 790485L, 785144L, 749133L, 722232L, 705868L, 704903L, 679764L, 675831L, 675075L, 666601L, 666001L, 654550L, 641478L, 636436L, 630729L, 627399L, 618889L, 617495L, 603159L, 599567L, 588712L, 585816L, 580350L, 570796L, 569448L, 560801L, 558804L, 549296L, 547908L, 532085L, 527237L, 526737L, 526272L, 521921L, 518093L, 514350L, 509913L, 495342L, 492939L, 485940L, 485255L, 484364L, 478023L, 466957L, 466114L, 459271L, 458035L])

def powerlaw(p,x):
	a,c=p
	return c*x**(-a)

def residuals(p,y,x):
	return y-powerlaw(p,x)

def plot_data(text_x):
	p0=[1,1]
	y1=test_x
	x=np.linspace(1,len(y1),len(y1))
	plsq=leastsq(residuals, p0, args=(y1, x)) 
	print u"拟合参数", plsq[0] # 实验数据拟合后的参数

	fig=figure(1)
	fig2=figure(2)
	fig3=figure(3)
	# ax1 = fig.add_subplot(3,1,1)
	# ax1.plot(x, y1) 
	# ax1.plot(x, powerlaw(plsq[0],x), label=u"fit") 

	ax2 = fig.add_subplot(2,1,1)
	ax2.plot(x,powerlaw(plsq[0],x),label=u"fit") 
	ax2.scatter(x,y1,s=50,color='r',edgecolor='')
	ax2.set_xlim(0,100)
	ax3 = fig.add_subplot(2,1,2)
	ax3.loglog(x,powerlaw(plsq[0],x),label=u"fit")
	ax3.loglog(x,y1,'ro')
	# ax1.grid(True)
	ax2.grid(True)
	ax3.grid(True)


	t1=fig2.add_subplot(1,1,1)
	t1.plot(x,powerlaw(plsq[0],x),label=u"fit") 
	t1.scatter(x,y1,s=50,color='r',edgecolor='')
	t1.set_xlim(0,100)
	t1.set_xlabel("index")
	t1.set_ylabel("popular degree")
	t1.legend(['fit','origin'])
	t1.grid(True)

	t2=fig3.add_subplot(1,1,1)
	t2.loglog(x,powerlaw(plsq[0],x),label=u"fit")
	t2.loglog(x,y1,'ro')
	t2.set_xlabel("index")
	t2.set_ylabel("popular degree")
	t2.legend(['fit','origin'])
	t2.grid(True)

	show()
# ---------------------
# # -*- coding: utf-8 -*- 
# import numpy as np 
# from scipy.optimize import leastsq
# import pylab as pl 
# def func(x, p): 
#   """ 数据拟合所用的函数: A*sin(2*pi*k*x + theta) """ 
#     A, k, theta = p 
#     return A*np.sin(2*np.pi*k*x+theta) 
# def residuals(p, y, x): 
#   """ 实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数 """ 
#     return y - func(x, p) 
# x = np.linspace(0, -2*np.pi, 100) 
# A, k, theta = 10, 0.34, np.pi/6 # 真实数据的函数参数 
# y0 = func(x, [A, k, theta]) # 真实数据 
# y1 = y0 + 2 * np.random.randn(len(x)) # 加入噪声之后的实验数据 
# p0 = [7, 0.2, 0] # 第一次猜测的函数拟合参数 
# # 调用leastsq进行数据拟合 
# # residuals为计算误差的函数 
# # p0为拟合参数的初始值 
# # args为需要拟合的实验数据 
# plsq = leastsq(residuals, p0, args=(y1, x)) 
# print u"真实参数:", [A, k, theta] 
# print u"拟合参数", plsq[0] # 实验数据拟合后的参数 
# pl.plot(x, y0, label=u"真实数据") 
# pl.plot(x, y1, label=u"带噪声的实验数据") 
# pl.plot(x, func(x, plsq[0]), label=u"拟合数据") 
# pl.legend() 
# pl.show()