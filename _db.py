#-*-coding:utf-8-*-
import MySQLdb
import datetime, calendar ,time

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

##################################
#  main process
#  import data to db

f = open('video_data_2010-2014.txt', 'r')

lines = f.readlines()

print len(lines)
print len(getDays("20101127","20141127"))
raw_input("asd")
conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='sina',charset="utf8")
cursor=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
sql = "insert into sina_top_video(date,comments,view) values(%s,%s,%s)"
i=0
for date in getDays("20101127","20141127"):
    line=lines[i]
    i = i+1
    if i>=len(lines):
        break
    li = eval(line)
    for item in li:
		tmp=(date,item[0],item[1].replace(',', ''))
		cursor.execute(sql,tmp)
cursor.close()
conn.commit()
conn.close()
# end import
###################################