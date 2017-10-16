import bs4
import re
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook

import time
book = Workbook()
sheet = book.active

searchfield="SanDisk 32GB"
datalist=[]
def mainfun(my_url):
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	# print page_soup
	product_available=""
	product_name = page_soup.findAll("h1",{"class":"_3eAQiD"})[0].text
	product_price = page_soup.findAll("div",{"class":"_1vC4OE _37U4_g"})[0].text
	try:
		product_actualprice = page_soup.findAll("div",{"class":"_3auQ3N _16fZeb"})[0].text
	except:
		product_actualprice = "Not Available"
	try:
		product_discount = page_soup.findAll("div",{"class":"VGWI6T _3GXWnA"})[0].text
	except:
		product_discount = "No Discount on Flipkart"
		# product_discount = "0% off"
	try:
		product_warranty = page_soup.findAll("div",{"class":"_3h7IGd"})[0].text
	except:
		product_warranty = "No Warranty on Flipkart"
	try:
		product_rating = page_soup.findAll("div",{"class":"hGSR34 _2beYZw"})[0].text
	except:
		product_rating = "Not Rated"
	try:
		product_available = page_soup.findAll("div",{"class":"_3xgqrA"})[0].text
	except:
		product_available = "Available"
	update_time = time.asctime(time.localtime(time.time()))
	# if int(product_discount.split("%")[0]) >=20:
	print "Product Name  : "+ product_name
	print "Product Rating: "+ product_rating
	print "Product Cost  : "+ product_price
	print "Actual Price  : "+ product_actualprice
	print "Discount Price: "+ product_discount
	print "Warranty      : "+ product_warranty
	print "Availablity   : "+ product_available
	print "Product Url   : "+ my_url
	print "Update Time   : "+ update_time
	print"------------------------------------------------"
	# sheet.append(datalist)
	# excelfilename = my_url.replace('https://','').replace('.','').replace('?','').replace('/',' ')
	# book.save(excelfilename)



baselink="https://www.flipkart.com"
bulklinks=[]
my_url=baselink+"/search?q="+searchfield+"&otracker=start&as-show=off&as=off"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
product_name = page_soup.findAll("a",{"class":"_1UoZlX"})
if product_name == []:
	product_name = page_soup.findAll("a",{"class":"_2cLu-l"})
for link in product_name:
		bulklinks.append(baselink+link.get('href'))

for l in bulklinks:
	mainfun(l)