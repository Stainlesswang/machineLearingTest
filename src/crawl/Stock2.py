'''
爬取深圳B类股票用的
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
# 截取公司名称
def getCompanyName(str): 
    new=  str.split("<u>")[-1].split("</u>")[0]
    return clearnStr(new)
# 清空空格
def clearnStr(new): 
    return new.replace(' ','')

def isContainsCompany(companyCode):
    sqlSelct='select * from stock_info where companyCode='+companyCode
    return mysql.update(sqlSelct)
def updateBycompany(companyCode,param=[]):
#     "aCode,aName,aMarketTime,aTotalStock,aCirculatingStock,type"
    print(param)
    updateSelct='update stock_info  set bCode=%s,bName=%s,bMarketTime=%s,bTotalStock=%s,bCirculatingStock=%s,type=3 where companyCode= '+companyCode
    return mysql.update(updateSelct,param)
mysql =MySql()
# print(isContainsCompany('300742'))
sql='insert into stock_info (companyCode, companyName,bCode,bName,bMarketTime,bTotalStock,bCirculatingStock,industry,type,belong) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
while var == 1:
#     jsonUrlA="http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1110&TABKEY=tab1&PAGENO="+str(stopPositon)
    jsonUrlB="http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1110&TABKEY=tab2&PAGENO="+str(stopPositon)
    response=request.urlopen(jsonUrlB)
    resultstr=json.loads(response.read().decode('UTF-8'))
    len_dat=len(resultstr[1]["data"])
    if len_dat>0:
        curr=[]
        for i in range(0,len_dat):
            if isContainsCompany(resultstr[1]["data"][i]["zqdm"])>0:
                temp=[]
                print('当前有该公司了,只更新当前这条数据')
                temp.append(resultstr[1]["data"][i]["bgdm"])
                temp.append(clearnStr(resultstr[1]["data"][i]["bgjc"]))
                temp.append(resultstr[1]["data"][i]["bgssrq"])
                temp.append(change(resultstr[1]["data"][i]["bgzgb"]))
                temp.append(change(resultstr[1]["data"][i]["bgltgb"]))
                
                updateBycompany(resultstr[1]["data"][i]["zqdm"],temp )
            else:
                print('执行增加操作,进行拼装数据')
                values = (resultstr[1]["data"][i]["zqdm"], getCompanyName(resultstr[1]["data"][i]["gsjc"]),
                      resultstr[1]["data"][i]["bgdm"], clearnStr(resultstr[1]["data"][i]["bgjc"]),
                      resultstr[1]["data"][i]["bgssrq"], change(resultstr[1]["data"][i]["bgzgb"]),
                      change(resultstr[1]["data"][i]["bgltgb"]), clearnStr(resultstr[1]["data"][i]["sshymc"]),2,2)
                curr.append(values)             
        returncode=mysql.insertMany(sql, curr);
        stopPositon+=1
        if returncode<=0:
            break
        time.sleep(1)
        print("下一页为:") 
        print(stopPositon)
        ime=time.time() 
        print("IO插入数据库时间为:") 
        print(ime-start)      
    else:
        print('没有数据了  退出while 循环')
        break
mysql.dispose()
end=time.time()
print("总共时间为时间为:") 
print(end-start)