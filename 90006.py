import csv
from bs4 import BeautifulSoup
import requests
import pandas as pf
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import calendar
import time,datetime

now_date = time.strftime("%Y%m%d")
day=int(now_date[-2:])


n_days1=5#五天前
for i in range(0,n_days1):
    

    now = datetime.datetime.now()
    delta = datetime.timedelta(days=i)
    n_days = now-delta
    now1=now.strftime('%Y%m%d')
    
    n_days1=n_days.strftime('%Y%m%d')
    c=str(n_days1[-4:-2])#幾月
    d=int(c)
    a=str(n_days1[-2:])#幾號
    b=int(a)

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver =webdriver.Chrome(chrome_options=options)


# driver.get(url)

page=0
with open('90006五天新聞.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('時間','類別','標題',['連結']))
    for i in range(5):

        r=driver.get("https://www.ettoday.net/news/news-list-2020-"+str(d)+"-"+str(b)+"-0.htm")
        
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_time=sp.select("div.part_list_2 > h3 > span")
        search_a=sp.select("div.part_list_2 > h3 > em")
        search_b=sp.select("div.part_list_2 > h3 > a")
        # search_c=sp.select("div.part_list_2 > h3 > a")
        
        for i in range(len(search_time)):
            
            print(search_time[i].text,end=' ')
            print(search_a[i].text,end=' ')
            print(search_b[i].text,end=' ')
            print(search_b[i].get('href'))
            writer.writerow([search_time[i].text,search_a[i].text,search_b[i].text,search_b[i].get('href')])
        b=b+1




 
    


driver.close()               #關閉瀏覽器


