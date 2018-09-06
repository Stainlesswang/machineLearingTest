# coding=utf-8
"""
当前为插入明星的操作
"""
from urllib import request
import json
import jsonpath
from dbConnection.MySqlConn import MySql
import time
mysql =MySql()

def isContainsCompany(name):
    sqlSelct='select * from ent_people_info where name='+"'"+name+"'"
    print(sqlSelct)
    return mysql.update(sqlSelct)
#开始时间
start=time.time()
stopPositon=0
var = 1
#保存value的 数组
ops = []
while var == 1:
    response=request.urlopen("https://wapbaike.baidu.com/api/starflower/getlistbyrange?rankType=all&weekType=thisWeek&start=0&stop="+str(stopPositon)+"&pos=up&qq-pf-to=pcqq.c2c")
    resultstr=json.loads(response.read().decode('UTF-8'))
    len_dat=len(resultstr["data"])
    if len_dat>0:
        for i in range(0, len_dat):
            values = (resultstr["data"][i]["name"], resultstr["data"][i]["picUrl"])
            if isContainsCompany(resultstr["data"][i]["name"])>0:
                print("已经有这个名字的明星了. 不在做添加操作!!!!")
            else:
                ops.append(values)
            
        print(stopPositon)
        stopPositon+=20
        time.sleep(1)
    else:
        print("获取JSON结束的耗费时间为:")
        ime=time.time() 
        print(ime-start)
        print(len(ops))    
        break
sql='insert into ent_people_info (name, photo) values (%s, %s)'
mysql.insertMany(sql, ops);
mysql.dispose()
end=time.time()
print("总共时间为时间为:") 
print(end-start)