#coding:utf-8

from bs4 import BeautifulSoup
import time
import threading
import random
import telnetlib,requests

#设置全局超时时间为3s，也就是说，如果一个请求3s内还没有响应，就结束访问，并返回timeout（超时）
import socket
socket.setdefaulttimeout(3)

headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
}

def get_ip():
    #获取代理IP，返回列表
    httpResult=[]
    httpsResult=[]
    try:
        for page in range(1,2):
            IPurl = 'http://www.xicidaili.com/nn/%s' %page
            rIP=requests.get(IPurl,headers=headers)
            IPContent=rIP.text
            print(IPContent)
            soupIP = BeautifulSoup(IPContent,'lxml')
            trs = soupIP.find_all('tr')
            for tr in trs[1:]:
                tds = tr.find_all('td')
                ip = tds[1].text.strip()
                port = tds[2].text.strip()
                protocol = tds[5].text.strip()
                if protocol == 'HTTP':
                    httpResult.append( 'http://' + ip + ':' + port)
                elif protocol =='HTTPS':
                    httpsResult.append( 'https://' + ip + ':' + port)
    except:
        pass
    return httpResult,httpsResult
'''
#验证ip地址的可用性，使用telnetlib模块_http
def cip(x,y):
    f = open("E:\ip_http.txt","a")
    f.truncate()
    try:
        telnetlib.Telnet(x, port=y, timeout=5)
    except:
        print('f')
    else:
        print('---------------------------success')
        f.write(x+':'+y+'\n')
#验证ip地址的可用性，使用telnetlib模块_https
def csip(x,y):
    f = open("E:\ip_https.txt","a")
    f.truncate()
    try:
        telnetlib.Telnet(x, port=y, timeout=5)
    except:
        print('f')
    else:
        print('---------------------------success')
        f.write(x+':'+y+'\n')
'''


#验证ip地址的可用性，使用requests模块，验证地址用相应要爬取的网页 http
def cip(x,y):
    f = open("ip_http.txt","a")
    f.truncate()
    try:
        print (x+y)
        requests.get('http://ip.chinaz.com/getip.aspx',proxies={'http':x+":"+y},timeout=3)
    except:
        print('f')
    else:
        print('---------------------------success')
        f.write(x+':'+y+'\n')
#验证ip地址的可用性，使用requests模块，验证地址用相应要爬取的网页。https
def csip(x,y):
    f = open("ip_https.txt","a")
    f.truncate()
    try:
        print (x+y)
        requests.get('http://s.manmanbuy.com/Default.aspx?key=%BF%DA%BA%EC&btnSearch=%CB%D1%CB%F7', proxies={'https':x+":"+y},timeout=3)
    except:
        print('f')
    else:
        print('---------------------------success')
        f.write(x+':'+y+'\n')




def main():
    httpResult,httpsResult = get_ip()

    threads = []
    open("ip_http.txt","a").truncate()
    for i in httpResult:
        a = str(i.split(":")[-2][2:].strip())
        b = str(i.split(":")[-1].strip())
        t = threading.Thread(target=cip,args=(a,b,))
        threads.append(t)

    for i in range(len(httpResult)):
        threads[i].start()
    for i in range(len(httpResult)):
        threads[i].join()



    threads1 = []
    open("ip_https.txt","a").truncate()
    for i in httpsResult:
        a = str(i.split(":")[-2][2:].strip())
        b = str(i.split(":")[-1].strip())
        t = threading.Thread(target=csip,args=(a,b,))
        threads1.append(t)

    for i in range(len(httpsResult)):
        threads1[i].start()
    for i in range(len(httpsResult)):
        threads1[i].join()



if __name__ == '__main__':
    main()