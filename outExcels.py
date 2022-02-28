'''
Author: crayonxin
Date: 2021-08-28 20:42:18
LastEditTime: 2022-02-28 15:40:59
LastEditors: crayonxin
Description: 
FilePath: \sdust_14_classroom\outExcels.py

'''

import bs4
from pandas.io import html
import requests as r
import pandas as pd

def getCookieDict(cook):
    cookies={}#初始化cookies字典变量
    for line in cook.split(';'):   #按照字符：进行划分读取
        #其设置为1就会把字符串拆分成2份
        if line!="":
            name,value=line.strip().split('=')
            cookies[name]=value  #为字典cookies添加内容
    return cookies

url="http://jwgl.sdust.edu.cn/jsxsd/kbcx/kbxx_classroom_ifr"
cookie_text="yikikata=1b3f1381-54df957b501e945f2a8b6eae619cb0b6; brmidyrvj=both; UM_distinctid=17e347770289ca-0fa89abc4d763d-4303066-144000-17e34777029abe; JSESSIONID=705D616322A32CB30FFAEA7804B03D21; yikikata=1b3f13d0-319c6a6c301f343c01eb03551046e48b; brmidyrvj=both"


def html_to_excel(d,index):
    res=r.post(url,data=d,cookies=getCookieDict(cookie_text))
    df=pd.read_html(res.text,encoding="utf-8")[0]
    print(df.shape)
    df.to_excel("excel/"+str(index)+".xlsx",encoding="utf-8")
    #print(response.text)


data={}
data["xnxqh"]="2021-2022-2"
data["xqid"]=1
data["jzwid"]=14
for i in range(18):# 本学期有18周
    data["zc1"]=i+1
    data["zc2"]=i+1
    html_to_excel(data,i+1)
