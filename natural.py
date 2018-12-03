import requests
from bs4 import BeautifulSoup
import urllib.request

urls = [
	#"http://www.data.ac.cn/zrzy/ntCB12.asp?d=&p=&g=&z=&query=+%C8%B7%C8%CF+&m=CB12&k=27&r=3&name=&pass=&danwei=",
	"http://www.data.ac.cn/zrzy/ntCB02.asp?p=&g=&z=&query=+%C8%B7%C8%CF+&m=CB02&k=27&r=1&name=&pass=&danwei="
	]
file = open('nature.csv', 'w')
f = open('python.txt', 'w')
for url in urls:
	page = urllib.request.urlopen(url)
	conts = page.read()
	
	#html方式获取所有数据
	so = BeautifulSoup(conts, 'html.parser')
	
	title_list = so.find_all('title')
	print(title_list)
	for title in title_list:
		nextstr = title.next
		print(title.string)
		file.write(title.string+'\n')
		body > center > div > center > center:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(8)
		body > center > div > center > center:nth-child(3) > table > tbody > tr:nth-child(3) > td:nth-child(2)
	table_list = so.find_all('table')
	for table in table_list[13:14]:
		tbody_list = table.find_all('tbody')
		#查找标签tr
		value_list = table.find_all('tr')
		print(len(value_list))
		print(len(value_list))
		print(len(value_list))
		
		#print(value_list[0])
		f.writelines(str(value_list))
		for value in value_list[:1]:
			te = value.text
			trr = value.find_all('tr')
			#print(trr[0])
			#print(len(trr))
			header_list = value.find_all('td')
			str = ""
			print(len(header_list))
			#获取所有td标签前十条数据
			for header in header_list[:9]:
				#对每条数据拆分，获取string部分，并拼接
				for td in header:
					if isinstance(td, int):
						print(td)
					if td.string:
						#print(td)
						str += td.string
				str += ','
			print(str)
			file.write(str+'\n')
		#	print(len(value))
		for value in value_list[1:]:
			str = ""
			#每条数据拆分重组
			for td in value:
				str += td.string+','
			file.write(str+'\n')

	#查找标签tr
	value_list = so.find_all('tr')
	#对表格抬头处理，只针对第16条数据
	for tr in value_list[15:16]:
		header_list = tr.find_all('td')
		str = ""
		#获取所有td标签前十条数据
		for header in header_list[:9]:
			#对每条数据拆分，获取string部分，并拼接
			for td in header:
				if td.string:
					str += td.string
			str += ','
		file.write(str+'\n')
	#获取17到62条数据（表格内容）
	for tr in value_list[16:62]:
		str = ""
		#每条数据拆分重组
		for td in tr:
			str += td.string+','
		file.write(str+'\n')
				
file.close()