#! /usr/bin/env python
# -*- coding: utf-8 -*-
##爬全球被黑站点统计 网站

import requests
import re
import time
from urlparse import *

for ii in range(1,180):
    url = 'http://www.hacker0day.com/index.php?page=%s'%str(ii)
    r= requests.get(url=url,timeout=3)
    con = r.text
    # result = re.findall(r'style="word-break:break-all"><a href="(.*?)" target="_blank">',con)
    result = re.findall(r'"_blank">([a-zA-z]+://[^\s]*)</a></td>', con)

    for i in result:
        print urlparse(i).netloc
        f = open("1.txt", "a+",)  # 把请求结果保存到1.
        f.write(urlparse(i).netloc+'\n')
        f.close()
    time.sleep(2)

# import requests,re
# from bs4 import BeautifulSoup
#
# url ='http://www.hacker0day.com/index.php?page=1'
#
# r = requests.get(url=url,timeout=2)
# con =r.text
#
# soup = BeautifulSoup(con,'lxml')
#
# result = soup.find_all(name='a',attrs={'href':re.compile('href="(.*?)" target="_blank"')})
#
# for i in result:
#     print i

