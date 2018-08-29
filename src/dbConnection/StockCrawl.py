'''
爬取深圳A类票信息
'''
from urllib import request
import json
from dbConnection.MySqlConn import MySql
import time
from decimal import *
#开始时间
start=time.time()
stopPositon=1
var = 1
#保存value的 数组
# ops = []

def change(string): 
    s=Decimal(string)*Decimal('100000000')
    return str(s).split(".")[0]
def isContainsCompany(companyCode):
    sqlSelct='select * from stock_info where companyCode='+companyCode
    return mysql.update(sqlSelct)
# 截取公司名称
def getCompanyName(str): 
    new=  str.split("<u>")[-1].split("</u>")[0]
    return clearnStr(new)
# 清空空格
def clearnStr(new): 
    return new.replace(' ','')
mysql =MySql()
sql='insert into stock_info (companyCode, companyName,aCode,aName,aMarketTime,aTotalStock,aCirculatingStock,industry,type,belong) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
while var == 1:
    jsonUrlA="http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1110&TABKEY=tab1&PAGENO="+str(stopPositon)
#     jsonUrlB="http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1110&TABKEY=tab2&PAGENO="+str(stopPositon)
    response=request.urlopen(jsonUrlA)
    resultstr=json.loads(response.read().decode('UTF-8'))
    len_dat=len(resultstr[0]["data"])
    if len_dat>0:
        curr=[]
        for i in range(0,len_dat):
            
            if isContainsCompany(resultstr[0]["data"][i]["zqdm"])>0:
                print("找到了重复数据***********")
                continue
            else:
                values = (resultstr[0]["data"][i]["zqdm"], getCompanyName(resultstr[0]["data"][i]["gsjc"]),
                      resultstr[0]["data"][i]["agdm"], clearnStr(resultstr[0]["data"][i]["agjc"]),
                      resultstr[0]["data"][i]["agssrq"], change(resultstr[0]["data"][i]["agzgb"]),
                      change(resultstr[0]["data"][i]["agltgb"]), clearnStr(resultstr[0]["data"][i]["sshymc"]),1,2)
#             ops.append(values)
                curr.append(values)
                
                
        returncode=mysql.insertMany(sql, curr);
        stopPositon+=1
        #执行一次插入  休眠一秒钟
        print(sql)
        print(curr)
        if returncode<=0:
            break
        time.sleep(1)
        print("下一页为:") 
        print(stopPositon)
        ime=time.time() 
        print("IO插入数据库时间为:") 
        print(ime-start) 
    else:
        break
mysql.dispose()
end=time.time()
print("总共时间为时间为:") 
print(end-start)




