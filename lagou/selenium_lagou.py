# -*- coding: utf-8 -*-


import time
from common.startBrower import *
from common.brower_act import *

import datetime


def loginLagou():

    # browser = startPhantomjs()
    browser = startChrome()
    # browser = startFirefox()

    browser.get("http://www.lagou.com")

    time.sleep(2)

    element_city = browser.find_element_by_xpath('/html/body//div[@id="changeCityBox"]//a[starts-with(@class,"tab") and text()="北京站"]')
    element_city.click()

    element_search_text = browser.find_element_by_xpath('//*[@id="search_input"]')

    element_search_text.send_keys('python')

    element_search = browser.find_element_by_xpath('//*[@id="search_button"]')
    element_search.click()
    time.sleep(2)

    return browser

#获取cookie
def getTokenFrom(browser):
    cookies = browser.get_cookies()
    transToCookie(cookies)
    saveCookiesLocal(cookies,'lagou_cookies.json')

#不在使用浏览器访问,而是直接使用url
data = {
    'first': 'true',
    'pn': 2,
    'kd': 'python'
}

def initLagouHeaders():
    # addHeader('Accept', 'application/json, text/javascript, */*; q=0.01')
    # addHeader('Accept-Encoding', 'gzip, deflate, br')
    # addHeader('Accept-Language', 'zh-CN,zh;q=0.9')
    # addHeader('Connection', 'keep-alive')
    # addHeader('Content-Length', '26')
    # addHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    # addHeader('Host','www.lagou.com')
    # addHeader('Origin', 'https://www.lagou.com')
    addHeader('Referer', 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=')
    # addHeader('X-Anit-Forge-Code', '0')
    # addHeader('X-Anit-Forge-Token', 'None')
    # addHeader('X-Requested-With', 'XMLHttpRequest')

def askJobData():
    initLagouHeaders()
    url_positionAjax = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'

    response = syncPost(url_positionAjax,data)
    print(response.text)


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    browser = loginLagou()
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)
    getTokenFrom(browser)
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)
    askJobData()