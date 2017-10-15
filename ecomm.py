import bs4
import re
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
import time
book = Workbook()
sheet = book.active

myurl="https://www.flipkart.com/redmi-note-4-lake-blue-64-gb/p/itmexfkvfnh26rxc?pid=MOBEXFKVEDPWPFVD&srno=s_1_6&otracker=search&lid=LSTMOBEXFKVEDPWPFVDZ5UOON&fm=SEARCH&iid=d37b0a03-a291-456e-95e1-3dcc69a9f1cb.MOBEXFKVEDPWPFVD.SEARCH&qH=0ebb2e8c32c9f552"

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

mainfun(myurl)