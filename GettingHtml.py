#-*- coding: utf-8 -*-
from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup
import sys

print('-----------')

try:
    html = urlopen("https://www.modetour.com/main/")
except HTTPError as e:
	print(e)
else:
	# html.read()함수로 html내용을 읽어들임
	bsObj = BeautifulSoup(html.read(), "html.parser")
	# html.parser는 파이썬에 기본적으로 내장되어있는 파서, html.parser대신에 lxml을 쓸 수도 있음


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

	print('type (body.h2): ', type(bsObj.body.h2))

