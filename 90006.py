import csv
from bs4 import BeautifulSoup
import requests
import pandas as pf
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime
import calendar
import time,datetime

now_date = time.strftime("%Y%m%d")
day=int(now_date[-2:])


n_days1=5
for i in range(0,n_days1):
    

    now = datetime.datetime.now()
    delta = datetime.timedelta(days=i)
    n_days = now-delta
    now1=now.strftime('%Y%m%d')
    
    n_days1=n_days.strftime('%Y%m%d')
    c=str(n_days1[-4:-2])
    d=int(c)
    a=str(n_days1[-2:])
    b=int(a)
url ="https://www.ettoday.net/news/news-list.htm"

key_word='0.0'
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver =webdriver.Chrome(chrome_options=options)
x = datetime.datetime.now()


driver.get(url)
for i in range(6):

    r = requests.get("https://www.ettoday.net/news/news-list-2020-"+str(d)+"-"+str(b)+"-0.htm")
    r.encoding = "utf8"
    with open('html.text', "w+",newline='', encoding="utf8") as fp:
    # print(r.text,file=fp)                                 ##可用print，也可用write
            fp.write(r.text)
    
    with open('html.text', "r", encoding="utf8") as fp2:
            r2=fp2.read() 
    
    page_source = r.text
    page_source2 = page_source.split('\n')
    soup = BeautifulSoup(r.text, "lxml")
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    
    tag_div1=soup.find_all('div',class_="part_list_2")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for a in tag_div1:
        print(a.text)
        list2.append(a.text)
        b=b+1


page=0
with open('90006五天新聞.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('時間','類別','標題',['連結']))

    for i in range(8):
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_time=sp.select("div.part_list_2 > h3 > span")
        search_a=sp.select("div.part_list_2 > h3 > em")
        search_b=sp.select("div.part_list_2 > h3 > a")
        search_c=sp.select("div.part_list_2 > h3 > a")
        
        for i in range(len(search_time)):
            
            print(search_time[i].text,end=' ')
            print(search_a[i].text,end=' ')
            print(search_b[i].get('href'))
            print(search_c[i].text,end=' ')
            writer.writerow([search_time[i].text,search_a[i].text,search_c[i].text,search_b[i].get('href')])
    


driver.close()               #關閉瀏覽器


