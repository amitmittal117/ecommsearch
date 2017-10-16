import bs4
import re
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
my_url="https://www.snapdeal.com/product/apple-iphone-6-64-gb/131798351#bcrumbSearch:iphone%206"
# my_url="https://www.snapdeal.com/product/apple-iphone-6-128-gb/652002997#bcrumbSearch:iphone%206"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
product_name = page_soup.findAll("h1",{"class":"pdp-e-i-head"})[0].text.split("\t\t\t")[-1]
product_cost = page_soup.findAll("span",{"class":"pdp-final-price"})[0].text
product_rating = page_soup.findAll("span",{"class":"avrg-rating"})[0].text
print product_name
print product_rating
print product_cost


