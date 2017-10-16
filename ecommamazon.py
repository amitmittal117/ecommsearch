import bs4
import re
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
import time
book = Workbook()
sheet = book.active
my_url = "https://www.amazon.in/Redmi-4-Black-32-GB/dp/B01NAKU5HE/ref=sr_1_1?s=electronics&ie=UTF8&qid=1508065437&sr=1-1&keywords=redmi+4"
# uClient = uReq(my_url)
# page_html = uClient.read()
# uClient.close()
# page_soup = soup(page_html, "html.parser")
# # print page_soup
# product_name = page_soup.findAll("span",{"class":"productTitle"})
# print product_name
excelfilename = my_url.replace('https://','').replace('.','').replace('/',' ')
print excelfilename