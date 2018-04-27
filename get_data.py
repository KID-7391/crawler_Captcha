#coding=utf8
import urllib.request
import json
import requests
import re
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import random
import pytz
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance
import pytesseract
from selenium.webdriver.common.keys import Keys
import sys
import numpy as np
import gc

test_source = 'http://s.manmanbuy.com/Default.aspx?key=%BF%DA%BA%EC&btnSearch=%CB%D1%CB%F7'
user_agent = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
]
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
           'Accept-Encoding': 'gzip, deflate',
           'Accept- Language': 'en - US, en;q = 0.5'
}

file_ip_https = open('ip_http.txt', 'r')
ip_list = file_ip_https.read().split('\n')
ip_list.pop()
file_ip_https.close()
def random_ip():
    ip = random.choice(ip_list)
    ip = ip.split(':')
    return ip

def recognize_Captcha(driver):
    try:
        driver.switch_to.frame(driver.find_element_by_id('iframeId'))
        driver.switch_to.frame(driver.find_element_by_id('iframemain'))
        time.sleep(1)
        input_yanzheng = driver.find_element_by_id('txtyz')
        print('find Captcha')
        while (1):
            img_src = driver.find_element_by_id('ImageButton3').screenshot_as_png
            # img_gray = img_src.convert('L')
            # img_sharp = ImageEnhance.Contrast(img_gray).enhance(2.0)
            img_sharp = img_src

            # save Captcha
            file_img = open('yanzhengma.png', 'bw+')
            file_img.write(img_src)
            file_img.close()

            img = cv2.imread('yanzhengma.png')
            # get rid of frame
            img = img[1:20, 1:56]

            # get rid of noise
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_gray = cv2.medianBlur(img_gray, 3)
            ret, img_binary = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
            cv2.imwrite('img_code.bmp', img_binary)

            # recognize
            code = pytesseract.image_to_string(Image.open('img_code.bmp'), lang='eng')
            code = code.replace(' ', '')
            print(code)
            input_yanzheng.send_keys(code)
            time.sleep(2)
            driver.find_element_by_name('yanzheng').send_keys(Keys.ENTER)
            time.sleep(2)
            try:
                input_yanzheng = driver.find_element_by_id('txtyz')
            except:
                driver.switch_to.default_content()
                break

    except:
        driver.switch_to.default_content()

def get_data_one_page(source, options, page):
    key1 = 'a href="http://tool\.manmanbuy\.com/historyLowest\.aspx?.+" target'
    key2 = 'a href="http://www\.manmanbuy\.com/disSitePro.+" v'
    r = requests.get(source, headers=headers)
    pattern1 = re.compile(key1)
    pattern2 = re.compile(key2)
    html = r.text
    file = open('source', 'w+')
    file.write(html)
    url = []
    list1 = re.findall(pattern1, html)
    list2 = re.findall(pattern2, html)
    for i in list1:
        i = i.replace('a href="', '')
        i = i.replace('" target', '')
        url.append(i)
    for i in list2:
        i = i.replace('a href="', '')
        i = i.replace('" v', '')
        url.append(requests.get(i).url)

    cnt = 0
    pattern_token = re.compile('token=.+')

    agent = random.choice(user_agent)
    headers['User-Agent'] = random.choice(agent)
    # ip = ['183.159.82.25', '18118']
    ip = random_ip()
    options.add_argument('user-agent="' + agent + '"')
    options.add_argument('--proxy-server=http://' + ip[0] + ':' + ip[1])
    driver = webdriver.Firefox(firefox_options=options)
    driver.set_page_load_timeout(8)

    i = -1
    try_time = 3
    while(i < len(url) - 1):
        i += 1
        this_url = url[i]
        if i % 5 == 4:
            driver.quit()
            del driver
            gc.collect()
            start = time.time()
            agent = random.choice(user_agent)
            headers['User-Agent'] = random.choice(agent)
            # ip = ['183.159.82.25', '18118']
            ip = random_ip()
            options.add_argument('user-agent="' + agent + '"')
            options.add_argument('--proxy-server=http://' + ip[0] + ':' + ip[1])
            driver = webdriver.Firefox(firefox_options=options)
            driver.set_page_load_timeout(8)
            end = time.time()
            print('time1:', end - start)
        try:
            driver.get(this_url)
        except:
            if try_time:
                i -= 1
                try_time -= 1
            continue
        # check if Captcha appears
        start = time.time()
        recognize_Captcha(driver)
        end = time.time()
        print('time2', end - start)

        start = time.time()
        # get token
        proxy = {'https': 'https://' + ip[0] + ':' + ip[1]}
        ret = driver.find_element_by_id('iframeId').get_attribute('src')
        token = re.findall(pattern_token, ret)
        json_url = this_url.replace('http://tool.manmanbuy.com/historyLowest.aspx?', '')
        json_url = json_url.replace('item.tmall', 'detail.tmall')
        json_url = 'http://tool.manmanbuy.com/history.aspx?DA=1&action=gethistory&' + \
                   json_url + '&bjid=&spbh=&cxid=&zkid=&w=951&' + token[0]

        try:
            data = requests.get(json_url, proxies=proxy, headers=headers)
            data = json.loads(data.text)
        except:
            if try_time:
                i -= 1
                try_time -= 1
            continue
        end = time.time()
        print('time3', end - start)

        start = time.time()
        if not ('spUrl' in data) or data['spUrl'] == 'https://detail.tmall.com/item.htm?id=544471454551':
            json_url = json_url.replace('detail.tmall', 'item.tmall')
            try:
                data = requests.get(json_url, proxies=proxy, headers=headers)
                data = json.loads(data.text)
            except:
                if try_time:
                    i -= 1
                    try_time -= 1
                continue

        if 'spName' in data:
            print(data['spName'])

        if not ('spUrl' in data) or data['spUrl'] == 'https://detail.tmall.com/item.htm?id=544471454551':
            if try_time:
                i -= 1
                try_time -= 1
            else:
                file = open('data/error_data_' + str(page) + '_' + str(cnt), 'w')
                file.write(json_url+'\n')
                file.write(data['datePrice']+'\n')
                file.close()
            continue
        else:
            file = open('data/data_' + str(page) + '_' + str(cnt), 'w')
            if 'spName' in data:
                file.write(data['spName']+'\n')
            file.write(data['datePrice']+'\n')
            file.close()
        cnt += 1
        try_time = 3
        end = time.time()
        print('time4', end - start)

    driver.quit()
    del driver
    gc.collect()

def get_data():
    print('firefox start')
    options = webdriver.FirefoxOptions()
    options.set_headless()
    source = 'http://s.manmanbuy.com/Default.aspx?key=%BF%DA%BA%EC&btnSearch=%CB%D1%CB%F7'
    while(1):
        ip = random_ip()
        print(ip)

        options.add_argument('--proxy-server=http://' + ip[0] + ':' + ip[1])
        driver = webdriver.Firefox(firefox_options=options)
        try:
            driver.get(source)
        except:
            time.sleep(2)
            continue
        break

    print('pass')

    file_page = open('file_page', 'r')
    current_page = file_page.read()
    if current_page != '':
        current_page = int(current_page)
        while(1):
            while (1):
                ip = random_ip()
                print(ip)

                options.add_argument('--proxy-server=http://' + ip[0] + ':' + ip[1])
                driver = webdriver.Firefox(firefox_options=options)
                try:
                    driver.get(source)
                except:
                    time.sleep(2)
                    continue
                break

            try:
                pagenum = driver.find_element_by_id('pagenum')
            except:
                print('fail')
                time.sleep(2)
                continue
            break
        pagenum.send_keys(current_page + 1)
        button = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[3]/div[5]/input[2]')
        # time.sleep(1)
        button.click()
        source = driver.current_url
    else:
        current_page = 0
    file_page.close()

    get_data_one_page(source, options, current_page)
    while(current_page <= 1200):
        current_page += 1
        file_page = open('file_page', 'w+')
        file_page.write(str(current_page))
        print(str(current_page))
        file_page.close()

        while (1):
            driver.quit()
            del driver
            gc.collect()
            ip = random_ip()
            options.add_argument('--proxy-server=http://' + ip[0] + ':' + ip[1])
            driver = webdriver.Firefox(firefox_options=options)
            try:
                driver.get(source)
            except:
                time.sleep(2)
                continue
            break

        pagenum = driver.find_element_by_id('pagenum')
        pagenum.send_keys(current_page + 1)
        button = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[3]/div[5]/input[2]')
        button.click()
        cnt_error = get_data_one_page(source, options, current_page)

    driver.close()


#
if __name__ == '__main__':
    old = sys.stdout
    sys.stdout = open('log', 'r+')
    get_data()



