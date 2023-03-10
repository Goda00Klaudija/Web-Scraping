# -*- coding: utf-8 -*-
"""***.ipynb

Automatically generated by Colaboratory.

Scrapped out zoopla.co.uk of 400 pages
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"
headers = {"user-agent": USER_AGENT}
ZooplaList = []

def getList(tag, num):
  url = f"https://www.zoopla.co.uk/to-rent/property/{tag}/?page_size=25&price_frequency=per_month&price_max=2000&q=london&radius=0&results_sort=newest_listings&search_source=facets&pn={num}"
  page = requests.get(url, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')
  lists = soup.find_all('div', class_="e1b8efd71 css-qnv97e-Wrapper-ListingCard-StyledListingCard e9kuaf115")
  for list in lists:
    Title = list.find('h2', class_ = "css-3h0n4w-Heading2-AddressTitle e9kuaf120").text.replace('</p>', '')
    Address = list.find('p', class_="css-1uvt63a-Address e9kuaf11").text.replace('</p>', '')
    Price = list.find('p', class_="css-xz7r6w-Price e9kuaf13").text.replace('</p>', '')
    Sub_Price = getattr(list.find('p', class_="css-1ikaqcj-Rent e9kuaf12"), 'text', None)
    Bed = list.find('div', class_="ejjz7ko0 css-1bzp01z-Wrapper-IconAndText e3e3fzo1").text.replace('</p>', '')
    info = [Title, Address, Price, Sub_Price, Bed]
    ZooplaList.append(info)
  return

for x in range(1,400):
  getList('london', x)

print(ZooplaList)

df = pd.DataFrame(ZooplaList)

df.to_excel('housing1.xlsx')
