# -*- coding: utf-8 -*-

from common.brower_act import *
import time
import os


url_index = "https://www.lagou.com"

url_collect_1 = ("https://a.lagou.com/collect?v=1&_v=j31&a=1066509849&t=pageview&_s=1&dl=https%3A%2F%2Fwww.lagou.com%2F&ul=zh-cn&de=UTF-8" 
              "&dt=%E6%8B%89%E5%8B%BE%E7%BD%91-%E4%B8%93%E4%B8%9A%E7%9A%84%E4%BA%92%E8%81%94%E7%BD%91%E6%8B%9B%E8%81%98%E5%B9%B3%E5%8F%B0" 
              "&sd=24-bit&sr=1920x1080&vp=1856x917&je=0&_u=MEAAAAQBK~&jid=355349021&cid=604188339.1551787385&tid=UA-41268416-1&_r=1&z=1782981357")

url_ajaxLogin = "https://passport.lagou.com/ajaxLogin/login.html?fl=1&service=https%3A%2F%2Fwww.lagou.com%2F&osc=PASSPORT._ascb(0)&ofc=PASSPORT._afcb(0)&pfurl=https%3A%2F%2Fwww.lagou.com%2F"

url_collect_2 = 'https://a.lagou.com/collect?v=1&_v=j31&a=1540383067&t=pageview&_s=1&dl=https%3A%2F%2Fwww.lagou.com%2F&dr=https%3A%2F%2Fwww.lagou.com%2F&ul=zh-cn&de=UTF-8&dt=%E6%8B%89%E5%8B%BE%E7%BD%91-%E4%B8%93%E4%B8%9A%E7%9A%84%E4%BA%92%E8%81%94%E7%BD%91%E6%8B%9B%E8%81%98%E5%B9%B3%E5%8F%B0&sd=24-bit&sr=1920x1080&vp=1795x824&je=0&_u=MACAAAQBK~&jid=&cid=651532055.1552025540&tid=UA-41268416-1&z=802568978'

url_smjod = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

url_positionAjax = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'

proxies = {
    'https': "https://127.0.0.1:8888"
}


job_type = 'python'
pageNo = 1
data = {
    'first': 'true',
    'pn': pageNo,
    'kd': job_type
}


def customSend():

    setProxie(proxies)
    cookies = None
    if os.access('lagou.json', os.F_OK):
        cookies = readCookiesLocal('lagou.json')
    if cookies is None :

        response = syncGet(url_index)

        #下面两个cookie加不加不影响爬虫成功
        # addCookie('a.lagou.com','.lagou.com','_ga','GA1.2.382307124.1552021196')
        # addCookie('a.lagou.com','.lagou.com','_gat','1')

        response = syncGet(url_collect_1)

        # print(printCookies())

        response = syncGet(url_ajaxLogin)

        response = syncGet(url_collect_2)

        response = syncGet(url_smjod)


        addHeader('Referer', 'https://www.lagou.com/jobs/list_'+job_type+'?labelWords=&fromSearch=true&suginput=''')
        # addHeader('Host', 'https://www.lagou.com')
        saveCookiesLocal(getAllCookies(),'lagou.json')
    else:
        addHeader('Referer', 'https://www.lagou.com/jobs/list_'+job_type+'?labelWords=&fromSearch=true&suginput=''')
        transToCookie(cookies)

    response = syncPost(url_positionAjax, data)

    print(response.content.decode('utf-8'))


    # url_ajax_searchJob = 'https://a.lagou.com/collect?v=1&_v=j31&a=455136169&t=pageview&_s=1&dl=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D&dr=https%3A%2F%2Fwww.lagou.com%2F&ul=zh-cn&de=UTF-8&dt=%E6%89%BE%E5%B7%A5%E4%BD%9C-%E4%BA%92%E8%81%94%E7%BD%91%E6%8B%9B%E8%81%98%E6%B1%82%E8%81%8C%E7%BD%91-%E6%8B%89%E5%8B%BE%E7%BD%91&sd=24-bit&sr=1920x1080&vp=1795x820&je=0&_u=MACAAAQBK~&jid=&cid=651532055.1552025540&tid=UA-41268416-1&z=497721973'
    #
    #
    # response = syncGet(url_ajax_searchJob)
    #
    # print(response.text)
    #
    # url_active = 'https://activity.lagou.com/activityapi/icon/getIcon.json?callback=jQuery111308794269018534482_1551859138953&companyIds=166345%2C85040%2C100530%2C102234%2C14093%2C30608%2C104269%2C432420%2C140241%2C23687%2C520217%2C221192%2C113856%2C55446%2C8103&markLocation=PPQ&_=1551859138955'
    #
    # response = syncPost(url_ajax_searchJob)
    #
    # print(response.text)

def sesionSend():
    session = requests.session()
    headers = getHeaders()
    session.headers.update(headers)
    response = session.get(url_index,proxies=proxies,verify=False)
    response = session.get(url_collect_1,proxies=proxies,verify=False)
    response = session.get(url_ajaxLogin,proxies=proxies,verify=False)
    response = session.get(url_collect_2,proxies=proxies,verify=False)
    session.headers.update({'Referer': 'https://www.lagou.com/jobs/list_'+job_type+'?labelWords=&fromSearch=true&suginput='})
    response = session.get(url_smjod,proxies=proxies,verify=False) #,proxies=proxies,verify=False, timeout=10
    # print(response.content.decode('utf-8'))
    response = session.post(url_positionAjax,data=data, proxies=proxies,verify=False, timeout=10)
    print(response.content.decode('utf-8'))



if __name__ == '__main__':
    customSend()
    # sesionSend()