import bs4
import re
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook

my_url="http://www.ebay.in/itm/Apple-iPhone-5s-64GB-Space-Grey-BRAND-NEW-IMPORTED-WARRANTY/332182122269?_trkparms=%26rpp_cid%3D586a56abe4b041211133ed01%26rpp_icid%3D586a55f3e4b09d7ed18ce83d&rpp_cat_id=586a560be4b0babf72d75b35"
my_url="http://www.ebay.in/itm/New-Apple-iPhone-6S-16-GB-Space-Grey-Smartphone-Warranty/332154118954?_trkparms=%26rpp_cid%3D586a56abe4b041211133ed01%26rpp_icid%3D586a55f3e4b09d7ed18ce83d&rpp_cat_id=586a560be4b0babf72d75b35"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
# product_name = page_soup.findAll("h1",{"class":"it-ttl"})[0].text.split("Details about   ")[-1]
product_name = page_soup.findAll("h1",{"class":"it-ttl"})[0].text.split("Details about   ")[-1]
print product_name