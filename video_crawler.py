from topvideo_comments import *
import datetime, calendar 

def strtodatetime(datestr,format):
    return datetime.datetime.strptime(datestr,format)  

def datediff(beginDate,endDate):  
    format="%Y%m%d";  
    bd=strtodatetime(beginDate,format)  
    ed=strtodatetime(endDate,format)      
    oneday=datetime.timedelta(days=1)  
    count=0
    while bd!=ed:  
        ed=ed-oneday  
        count+=1
    return count  

def datetostr(date):    
    return   str(date)[0:10]  

def getDays(beginDate,endDate):  
    format="%Y%m%d";  
    bd=strtodatetime(beginDate,format)  
    ed=strtodatetime(endDate,format)  
    oneday=datetime.timedelta(days=1)   
    num=datediff(beginDate,endDate)+1   
    li=[]  
    for i in range(0,num):   
        li.append((bd).strftime("%Y%m%d"))  
        bd=bd+oneday  
    return li 

##############
#main process

for date in getDays("20141101","20141120"):
	print date
	get_video_data(date,1000)

print "done"