'''
Created on 2018年7月11日

@author: chinaso
'''
from urllib import request
import json
from dbConnection.MySqlConn import MySql
import time
from decimal import *


# def get_ip_list(self):
#        print("正在获取代理列表...")
#        url = 'http://www.xicidaili.com/nn/'
#        html = requests.get(url=url, headers=self.headers).text
#        soup = BeautifulSoup(html, 'lxml')
#        ips = soup.find(id='ip_list').find_all('tr')
#        ip_list = []
#        for i in range(1, len(ips)):
#            ip_info = ips[i]
#            tds = ip_info.find_all('td')
#            ip_list.append(tds[1].text + ':' + tds[2].text)
#        print("代理列表抓取成功.")
#        return ip_list
# 
# def get_random_ip(self,ip_list):
#     print("正在设置随机代理...")
#     proxy_list = []
#     for ip in ip_list:
#         proxy_list.append('http://' + ip)
#     proxy_ip = random.choice(proxy_list)
#     proxies = {'http': proxy_ip}
#     print("代理设置成功.")
#     return proxies
# headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
# headers=("Referer", "http://www.sse.com.cn/assortment/stock/list/share/")
# httpproxy_handler = request.ProxyHandler({"http" : "91.202.144.54:53281"})
# #创建一个opener
# opener=request.build_opener()
# opener.add_handler(httpproxy_handler)
# #将headers添加到opener中
# opener.addheaders=[headers]
# #将opener安装为全局
# request.install_opener(opener)
# urlmy='http://query.sse.com.cn/security/stock/getStockListData2.do?&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25&pageHelp.pageNo=1&_=1531295588196'
# 
# response=request.urlopen(urlmy)
# resultstr=json.loads(response.read().decode('UTF-8'))
# len_dat=len(resultstr[1]["data"])





def change(string): 
    
    s=Decimal(string)*Decimal('100000000')
    return str(s.split(".")[0])

print(change("19.89").split(".")[0])



























