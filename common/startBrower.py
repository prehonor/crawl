# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def startFirefox():
    location = 'D:/Program Files (x86)/Mozilla Firefox/firefox.exe'
    options = Options()
    # options.add_argument('-headless')
    browser = webdriver.Firefox(firefox_binary=location,firefox_options=options)
    return browser

def startChrome():
    location = 'D:/Anconda3/envs/tensorflow-gpu/chromedriver.exe'
    browser = webdriver.Chrome(executable_path=location)
    return browser

def startPhantomjs():

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
    location = 'D:/Program Files (x86)/phantomjs-2.1.1-windows/bin/phantomjs.exe'
    browser = webdriver.PhantomJS(executable_path = location,desired_capabilities=dcap)
    return browser