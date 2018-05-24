#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


headers={

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",

    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',

    'Connection' : 'keep-alive',

    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',

    'X-Forwarded-For':'120.239.169.74'
}

def url(key):

    for i in range(0,10,10):
        bd_search="https://www.baidu.com/s?word=%s=&pn=%s"% (key,str(i))
        # bd_search = "https://bbs.ichunqiu.com/thread-40592-1-1.html"
        r =requests.get(bd_search,headers=headers,verify=False,timeout=2)
        s= r.text
        # result = re.findall(r'.t > a',s)
        # print s.encode('utf-8')
        soup=BeautifulSoup(s,"lxml")

        url_list=soup.select(".t > a")   #对请求回来的内容进行查找，找出a标签里（找出URL链接）
        # print url_list
        for url in url_list:
            real_url=url['href']   #遍历循环，并且打印
            try:
                r=requests.get(real_url,headers=headers,verify=False,timeout=2)  #再次请求

                print(r.url)  #打印出URL链接
                print key
            except Exception as e:

                print(e)
# url('sss')
if __name__ == '__main__':
    command = sys.argv[1:]
    chanshu = "".join(command)

    url(chanshu)
