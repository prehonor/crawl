# -*- coding: utf-8 -*-

import requests
import re
import json

# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context



#消息头格式

_cookies = []

_proxies = {}

def setProxie(proxies):
    for key,value in proxies.items():
        _proxies[key] = value

class Cookie:
    _name=''
    _value=''
    _domain=''
    _host=''
    def __init__(self,name='',value='',domain='',host='') :
        _name = name
        _value = value
        _domain = domain
        _host = host
#消息头
_headers = {}

def getHeaders():
    return _headers

def init():
    _headers.setdefault('Accept','*/*')
    _headers.setdefault('Accept-Encoding','gzip, deflate, br')
    _headers.setdefault('Accept-Language','zh-CN,zh;q=0.9')
    _headers.setdefault('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36')
    _headers.setdefault('Cookie','')

init()


def addHeader(key,value):
    _headers[key] = value

def addCookie(host,domain,name,value):
    cookie = exitCookieOrCreate(host,domain,name,value)

def exitCookieOrCreate(host,domain,name,value):
    for i in _cookies:
        if i._domain == domain and i._name == name:
            return i
    cookie = Cookie()
    cookie._host = host
    cookie._name = name
    cookie._value = value
    cookie._domain = domain
    _cookies.append(cookie)
    return cookie

#将从真实浏览器中获取的cookie放入模拟浏览器请求的cookie中
def transToCookie(cookies):
    for i in cookies:
        addCookie('',i['domain'],i['name'],i['value'])

def parseHostFromUrl(url):
    matchObj = re.match( r'(https|http)://([^/]+)(/.*)?', url, re.M|re.I)
    if matchObj != None:
        return matchObj.group(2)
    else :
        raise Exception("没有匹配到Host!")


def repsSetCookies(host,cookies):
    for i in cookies:
        cookie = exitCookieOrCreate(host,i.domain,i.name,i.value)
        print("本次请求返回的cookie:"+ i.name+i.value)


def saveCookiesLocal(cookies,fileName):
    jsonCookies = json.dumps(cookies)
    with open(fileName, 'w') as f:
        f.write(jsonCookies)

#读取本地文件存储的cookie
def readCookiesLocal(fileName):
    listCookies = None
    with open(fileName, 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    return listCookies

def cookies2String(cookies):
    value_cookies = ''
    for key,value in cookies.items():
        value_cookies += key +'=' + value + ';'
    return value_cookies


#同步发送请求
def syncGet(url,proxies = None):
    host = parseHostFromUrl(url)
    cookieValue = cookies2String(getCookies(host))
    addHeader('Cookie',cookieValue)
    response = requests.get(url, headers = _headers, proxies= _proxies if (proxies is None) else proxies,verify=False)
    repsSetCookies(host,response.cookies)
    return response

#根据域名找到该域名和顶级域名下的cookie,实现有点麻烦,这里只根据拉勾网的特殊情况
def getCookies(host):
    cookie = {}
    for i in _cookies:
        if i._domain != '' and host != '' and  host.find(i._domain) >= 0 :
            cookie[i._name] = i._value
    return cookie

def getAllCookies():
    cookies = []
    for i in _cookies:
        cookie = {}
        cookie['domain'] = i._domain
        cookie['name'] = i._name
        cookie['value'] = i._value
        cookie['host'] = i._host
        cookies.append(cookie)
    return cookies
def syncPost(url,data,proxies = None):

    host = parseHostFromUrl(url)
    cookieValue = cookies2String(getCookies(host))
    print('本次请求cookie:'+cookieValue)
    addHeader('Cookie',cookieValue)
    response = requests.post(url,data=data, headers=_headers, proxies = _proxies if (proxies is None) else proxies,verify=False, timeout=10)
    return response


#异步发送
def asysGet():
    return 1


def printAllCookies():
    print(cookies2String(_cookies))