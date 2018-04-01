#-*- coding: utf-8 -*-
#from urllib2.request import urlopen
#from urllib2.request import HTTPError
from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup
import sys

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
	#print('==== full tag ====')
	#print(bsObj)
	#print('==== html ====')
	#print(bsObj.html)
	#print(bsObj.head)
	print(bsObj.head.title)
	print('==== h1 ====')
	print(bsObj.h1)
	print('==== h2 ====')
	print(bsObj.h2)
	print('==== body.h2 ====')
	print(bsObj.body.h2)
	print(bsObj.find_all('h2'))


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