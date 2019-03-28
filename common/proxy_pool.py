# -*- coding: utf-8 -*-

import time
from common.startBrower import *
import re
import json

import datetime

starttime = datetime.datetime.now()
'''
获取代理
'''

_url = ['https://www.kuaidaili.com/free/intr','https://www.xicidaili.com/wn','https://www.xicidaili.com/nt']
_proxies = {}
_index = 0

def getUrl():
    global _index
    index = _index % _url.__len__()
    _index +=1
    return _url[index]

def getProxies():
    url = getUrl()
    from common import brower_act
    response = brower_act.syncGet(url)
    print(response)
    return {}

def getProxiesByBrowser():
    proxies = []
    url = getUrl()
    browser = startPhantomjs()

    browser.get(url)
    time.sleep(3)

    for num in range(1,3):
        browser.get(url+'/'+ str(num) )
        tr_elements = browser.find_elements_by_xpath('//table//tr')
        for tr in tr_elements:
            text = tr.text
            if(notFilter(text)==True):
                proxies.append(parseText(text))

    return proxies

def saveLocal(proxies):
    jsonProxies = json.dumps(proxies)
    with open('proxies.json','w') as file:
        file.write(jsonProxies)

def parseText(text):
    regex_type = r'(https|http)'
    type = re.compile(regex_type,re.I).search(text).group()
    regex_ip = r'(\d+\.){3}\d+'
    ip = re.compile(regex_ip).search(text).group()
    regex_port = r'(?<!\d)\d{2,5}(?!\d)'
    port = re.compile(regex_port).search(text).group()
    return {type : ip+':'+port}

def notFilter(text):
    regex_seconds = r'(\d(\.\d{1,3})?)秒'
    temp = re.compile(regex_seconds,re.I).search(text)
    seconds = (None if (temp is None) else temp.group(1))
    if seconds == None :
        return False
    if float(seconds) < 2 :
        return True
    else :
        return False

"""
测试
"""
def main():
    getProxiesByBrowser()

if __name__ == '__main__':
    main()

