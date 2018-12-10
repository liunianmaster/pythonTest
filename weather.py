
#encoding:utf-8
   
import requests

from bs4 import BeautifulSoup

import pandas as pd
from aiohttp import web

#from urllib import request
import urllib.request

import _string

#import urllib2

import asyncio, os, json, time
                                                        
urls = ["http://lishi.tianqi.com/wuhan/201607.html",
		"http://lishi.tianqi.com/wuhan/201606.html",
		"http://lishi.tianqi.com/wuhan/201605.html"]
		
urltq = ["https://lishi.tianqi.com/wuhan/201607.html"]
		
url = ["http://tianqi.2345.com/wea_history/57036.htm"]

file = open('wuhan_weather.csv','w')
f = open('python.txt', 'w')
for url in urltq:
	
	
	
	#url = "http://www.tianqihoubao.com/lishi/shijiazhuang/month/201101.html"
	url = "http://lishi.tianqi.com/wuhan/201607.html"
	douban = "http://movie.douban.com/top250?format=text"
	www = "https://lishi.tianqi.com/"
	tiqian = "https://www.tianqi.com/"
	h234 = "http://tianqi.2345.com/wea_history/57036.htm"
	baidu = "https://www.baidu.com"
	zzmaster = "http://vote.zzmaster.club"
	suzhou = "http://tianqi.2345.com/suzhou/58357.htm"
	natural = "http://www.data.ac.cn/zrzy/ntCB02.asp?p=&g=&z=&query=+%C8%B7%C8%CF+&m=CB02&k=27&r=1&name=&pass=&danwei="
	ziran = 'http://www.data.ac.cn/zrzy/ntCB02.asp?p=&g=&z=&query=+%C8%B7%C8%CF+&m=CB02&k=27&r=1&name=&pass=&danwei='
	thisUrl = ziran
	page = urllib.request.urlopen(thisUrl)
	conts = page.read()
	#print(conts)
	
	so = BeautifulSoup(conts, "html.parser")
	weaValue = so.find_all('table',border='1')
	#body > center > div > center > center:nth-child(3) > table > tbody > tr:nth-child(1)
	print(len(weaValue))
	#for tb in weaValue:
	tb = weaValue[1]
	title_list = tb.find_all('tr', bgcolor='#00FFFF')
	for title in title_list:
		ui = []
		for i,td in enumerate(title):
			if i <= 10:
				print(td)
	
	value_list = so.find_all('tr')
	for i,tr in enumerate(value_list):
		ui = []
		if i <= 61 and i > 15:
			print(len(tr))
			for j,td in enumerate(tr):
				ui.append(td.string)
			#f.writelines(ui)
			print(ui)
	#weaValue = so.find(id = "day7info")
	
	#print(weaValue)
	
	#print(temp+humidity+pressure)
	his = weaValue.select("li")
	#print(his)
	
	#weather_tab = his.find("div", class_="data-table")
	#print(weather_tab)
	#ullist = weaValue.select('tr')
	#print(ullist)
	
	
	day7 = so.find(id = "day7info")
	day7list = day7.select("li")
	sel = 'day7info > ul > li:nth-child(1) > i > script'
	sc = so.find(sel)
	print(sc)
	dayul = day7.find('ul')
	li = dayul.select('li')
	f.writelines(str(day7))
	#print(li[1])
	#print(day7list)
	#for ul in day7list:
		
		#print(ul.get_text())
	
	#for ul in his:
		#print(ul.get_text())
		
	for ul in his:
		#print(ul.get_text())
		#li_list= ul.select('li')
		b = ul.find('h1').get_text()
		#print(b)
		blue = ul.find('font', class_='blue').get_text()
		red = ul.find('font', class_='red').get_text()
	#	print(blue+red)
		feng = ul.find('i').get_text().split(" ")
		#day8info > ul > li:nth-child(1) > i > font.red
		#day8info > ul > li:nth-child(1) > div
		#//*[@id="day7info"]/ul/li[1]/div/text()
		#//*[@id="day8info"]/ul/li[1]/div/text()
		#//*[@id="day7info"]/ul/li[1]/i/text()[2]
		
	#	print(feng[1]+feng[2])
	#	print(ul.get_text())
	
	
		
	#uldiv = weaValue.select('div')
	apilist = so.find_all(class_ = 'api_container')
	print(apilist)
	for api in apilist:
		wuran = api.get_text()
		print(wuran)
		
	#print(value_list)
	#print(temp)

	#print(so)
	for tag in so.find_all("td", {"class":"center"}):
		name = tag.find('span', class_='red').get_text()
		print(name)
		rating = (tag.find('span',class_='rating_num').get_text())
		#file.write(name+','+rating+'\n')
		if isinstance(name, str):
			#print("str")
			file.write("str"+'\n')
		if isinstance(name, dict):
			file.write("dict"+'\n')
		if isinstance(name, bytes):
			file.write("bytes"+'\n')
		if isinstance(name, web.StreamResponse):
			file.write("web"+'\n')
		#if len(tqtongji2) > 0:
			#file.write("len > 0"+'\n')
		else:
			file.write("other"+'\n')
		file.write(repr(name)+'\n')
		#print(repr(name)+', -- '+rating+'\n')
	
	
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,  like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
	# 设置头文件信息
	response = requests.get(url, headers=headers).text	#提交requests get 请求
	
	#response = requests.get(url)
	request_data = request.urlopen(url)
	#soup = BeautifulSoup(response, "html.parser")
	soup = BeautifulSoup(response, "lxml")
	#soup = BeautifulSoup(request_data, "html.parser")
	print(response)
	tqtongji2=soup.find("div",class_="tqtongji2")
	#tqtongji=soup.find("div",{"class":"tqtongji2"})
	#tqtongji2=soup.findAll("div",{"class":"wdetail"})
	
	#ul_all=tqtongji2.find_all("ul")
	#ul_all=soup.findAll("div",{"class":"wdetail"})

	#tqtongji2=soup.find("ul",{"class":"tl"})
	#tqtongji2=soup.findAll({"ul"})
	if isinstance(tqtongji2, str):
		file.write("str"+'\n')
	if isinstance(tqtongji2, dict):
		file.write("dict"+'\n')
	if isinstance(tqtongji2, bytes):
		file.write("bytes"+'\n')
	if isinstance(tqtongji2, web.StreamResponse):
		file.write("web"+'\n')
	#if len(tqtongji2) > 0:
		#file.write("len > 0"+'\n')
	else:
		file.write("other"+'\n')
	#ul_all=tqtongji2.find_all("ul")

	url = "https://lishi.tianqi.com/wuhan/201607.html"
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	#weather_list = soup.select('div[class="tqtongji2"]')
	weather_list = soup.find("div",{"class":"tqtongji2"})
	#weather_list = soup.select('div[id="weather_tab"]')
	#weather_list = soup.select('div[class="page"]')
	#<div class="data-table" id="weather_tab"
	file.write("url"+'\n'+url)
	#ul_list = weather_list.find_all("ul")
	#for weather in weather_list:
	
	file.write("weather"+'\n')
	#ul_list = weather.select('tr')
	#weather_date = weather.select('td')[0].string.encode('utf-8')
	#weather_date = weather.select('a')[0].string.encode('utf-8')
	#weather_date = weather.select('tr')
	#ul_list = weather.select('ul')
	
	i=0
	for ul in ul_list:
		li_list= ul.select('li')
		#li_list= ul.select('th')
		str=""
		for li in li_list:
			str += li.string.encode('utf-8')+','
		if i!=0:
			file.write(str+'\n')
		i+=1
	file.write("no values"+'\n')
file.close()