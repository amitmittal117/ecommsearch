import bs4
import re
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
import time
book = Workbook()
sheet = book.active

searchfield="Mi A1"

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
		product_available = page_soup.findAll("div",{"class":"_3xgqrA"})[0].text
	except:
		product_available = "Available"
	update_time = time.asctime(time.localtime(time.time()))
	print "Product Name: "+ product_name
	print "Product Cost: "+ product_price
	print "Availablity : "+ product_available
	print "Product Url : "+ my_url
	print "Update Time : "+ update_time




baselink="https://www.flipkart.com"
bulklinks=[]
my_url="https://www.flipkart.com/search?q="+searchfield+"&otracker=start&as-show=off&as=off"
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
	print"------------------------------------------------"