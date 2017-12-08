#-*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import sys


targetUrl = "http://aqicn.org/city/seoul/kr/"
html = urlopen(targetUrl).read()
# beautifulsoup 으로 파싱
soupData = BeautifulSoup(html, 'html.parser')
# 지역 정보를 읽어 오고.
titleData = soupData.find('a', id='aqiwgttitle1')
print('----------')
print(titleData.string)

# 미세먼지 수집 시간도 읽고
timeData = soupData.find('span', id='aqiwgtutime')
print(timeData.string)

# 마지막으로 미세먼지 수치를 읽는다.
aqiData = soupData.find('div', id='aqiwgtvalue')
print(aqiData.get('title'))
print(aqiData.string)


print('-----------')
# urllib.request 패키지의 urlopen()함수를 import.
# 웹페이지(url)에서 html객체를 초기화한다. 

# html.read()함수로 html내용을 읽어들인다.
# html.parser는 파이썬에 기본적으로 내장되어있는 파서라고 한다. html.parser대신에 lxml을 쓸 수도 있다고 한다.
try:
	#html = urlopen('http://www.pythonscraping.com/pages/page1.html')
    html = urlopen("https://www.modetour.com/main/")
except HTTPError as e:
	print(e)
else:
	bsObj = BeautifulSoup(html.read(), "html.parser")
	print(bsObj.h1)



'''
print('========')
#print(bsObj)
print('========')
#print(bsObj.html)
print('========')
#print(bsObj.h1)
#print(bsObj.html.body.h1)
#print(bsObj.html.h1)
#print('========')
'''