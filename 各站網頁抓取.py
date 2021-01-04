from selenium import webdriver
import csv
import requests
from bs4 import BeautifulSoup
import time,datetime
import sys

key=input("請輸入想買的東西:\n")

url="https://www.rakuten.com.tw/search/"+key+"/?s=2"
url2="https://www.momoshop.com.tw/search/searchShop.jsp?keyword="+key+"&searchType=2&curPage=1&_isFuzzy=0&showType=chessboardType"
url3="https://ecshweb.pchome.com.tw/search/v3.3/?q="+key+"&scope=all&sortParm=prc&sortOrder=ac"

options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=options)
driver.get(url)
html = driver.page_source
page=0
with open('期中考.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('time','類別','title',['url']))
    for i in range(3):   
      page+=1
      html = driver.page_source
      sp=BeautifulSoup(html,"html.parser")
      search_name=sp.select("div.product-info > a > h3")#商品名
      search_price=sp.select("div.product-info > a > div.product-price")#價格
      search_url=sp.select("div.product-info > a ")
      
      for i in range(len(search_name)):  
               # print(page)
               print(search_name[i].text,end=' ')
               print(search_price[i].text)
               print(search_url[i].get('href'))
               writer.writerow([search_name[i].text,search_price[i].text,search_url[i].get('href')])
time.sleep(2)

driver.get(url2)
page=0
with open('期中考.csv','a+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)

    for i in range(1):   
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_name=sp.select("div.prdInfoWrap > h3")#商品名
        search_price=sp.select("div.prdInfoWrap > p > span > b")#價格
        search_url=sp.select("div.listArea > ul > li > a")
        
        for i in range(len(search_name)):  
                # print(page)
                print(search_name[i].text,end=' ')
                print(search_price[i].text)
                print("https://www.momoshop.com.tw"+search_url[i].get('href'))
                writer.writerow([search_name[i].text,"$"+search_price[i].text,"https://www.momoshop.com.tw"+search_url[i].get('href')])
time.sleep(2)

driver.get(url3)
page=0
with open('期中考.csv','a+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
 
    for i in range(1):
          page+=1
          html = driver.page_source
          sp=BeautifulSoup(html,"html.parser")
          search_name=sp.select("div.Cm_C>dl>dd.c2f> h5>a")#商品名
          search_price=sp.select("div.Cm_C>dl>dd.c3f> ul>li>span")#價格
          search_url=sp.select("div.Cm_C>dl>dd.c2f> h5>a")
          
          for i in range(len(search_name)):  
            # print(page)
            print(search_name[i].text,end=' ')
            print(search_price[i].text)
            print("https:"+search_url[i].get('href'))
            writer.writerow([search_name[i].text,search_price[i].text,"https:"+search_url[i].get('href')])

time.sleep(2)  # 必須加入等待，否則會有誤動作
driver.close()        
        #關閉瀏覽器
with open('期末考.csv','r',newline='', encoding="utf-8-sig") as csvfile:  
    rows = csv.reader(csvfile)   #解決多一空行 newline=''
    a=[]
    for row in rows:
        a.append(row)
        a.sort(key=lambda s: s[1])

        headers = {
            "Authorization": "Bearer " + "7uL4cYgaNXqTRYBMpzkw1INZvsogSea7RQJJywCVDEP",
            "Content-Type": "application/x-www-form-urlencoded"
            }
        
            
 
    params = {"message": "名稱:\n"+a[0][0]+"\n"+"價格:"+a[0][1]+"\n"+"網址\n"+a[0][2]}  
      
    r = requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)
    print(r.status_code)  #200
sys.exit    
