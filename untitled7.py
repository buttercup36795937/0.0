import requests
import csv
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium .webdriver.support.ui import Select

# r = requests.get("https://udn.com/news/story/7321/5018383?from=udn_ch2_menu_v2_main_index")
r = requests.get("https://udn.com/news/story/6813/5020920")
r.encoding = "utf8"

with open('html.txt', "w", encoding="utf8") as fp:
    print(r.text,file=fp)                                 ##可用print，也可用write
    fp.write(r.text)
    
with open('html.txt', "r", encoding="utf8") as fp2:
    r2=fp2.read() 
    
page_source = r.text
page_source2 = page_source.split('\n')

soup = BeautifulSoup(r.text, "lxml")
list1=[]
list2=[]
tag_div=soup.find("div",class_="article-content")
print(tag_div)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for a in tag_div:
    print(a.text)
list1.append(a.text)


csvfile="1.csv"
with open(csvfile,"w",newline='',encoding="utf-8-sig")as fp:
    writer=csv.writer(fp)
    writer.writerow([list1[0],list2[0]])