import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.naver.com"

req=requests.get(url)
html = req.text

# python 내장 함수 html.parser
soup = BeautifulSoup(html, 'html.parser')
templist = soup.select('div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li')


a=[]
for temp in templist:
    a.append(temp.text)

ranklist = []
num=1
for i in a:
    if num>9:
        ranklist.append(i[5:-2])
    else:
        ranklist.append(i[4:-2])
    num+=1

for k,list in enumerate(ranklist):
    print(str(k+1)+"위 "+list)


# print(a)