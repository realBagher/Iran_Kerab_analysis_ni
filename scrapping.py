import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import csv
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
url = "https://www.iranketab.ir/book/43-a-fraction-of-the-whole"

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all('table',{'class':'product-table'})
for i in books:
    book_code = i.find("td")
    a = book_code.find_next('td')
    book_code = book_code.find_next('td').text.strip()
    
    translator = a.find_next("td")
    a = translator.find_next('td')
    translator_id = a.find('a')
    link = translator_id['href']
    translator_id = re.search(r"/(\d+)-", link)
    translator = a.text.strip()
    
    shabak = a.find_next("td")
    a = shabak.find_next("td")
    shabak = a.text.strip()
    
    qate = a.find_next("td")
    a = qate.find_next("td")
    qate = a.text.strip() 
    
    num_pages =a.find_next("td")
    a = num_pages.find_next("td")
    num_pages = qate = a.text.strip()
    
    pub_year_shamsi = a.find_next("td")
    a = pub_year_shamsi.find_next("td")
    pub_year_shamsi = a.text.strip() 
    
    pub_year_miladi = a.find_next("td")
    a = pub_year_miladi.find_next("td")
    pub_year_miladi = a.text.strip()
    
    jeld_type = a.find_next("td")
    a = jeld_type.find_next("td")
    jeld_type = a.text.strip()
    
    series_name = a.find_next("td")
    a = series_name.find_next('td')
    series_name = a.text.strip()
    

    