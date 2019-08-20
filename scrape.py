#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:14:02 2019  
@author: nightking
"""
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys


driver = webdriver.Chrome('/home/nightking/Downloads/chromedriver')
driver.get("https://www.capterra.com")
def search_product(product):
    url = 'https://www.capterra.com'
    base_url = 'https://www.capterra.com/search/?search='
    product = product.split(' ')
    for x in range(len(product)):
        base_url = base_url + '+' + product[x]
    driver.get(base_url)
    soup = driver.page_source
    soup = BeautifulSoup(soup)
    soup = soup.find_all('div',{'class':'Product__ProductResultsContainer-u8wvrl-2 kDutpy StyledProductResultContainer-ze7tzb-0 iVyAPY'},href=True)   
    link = []
    name = []
    for x in range(len(soup)):
        link.append(url + soup[x]['href'])
        name.append(soup[x]['href'].split('/')[-1])
    product = list(zip(name,link))
    return product



def get_reviews(product):
    
product = ('Google-Docs', 'https://www.capterra.com/p/160756/Google-Docs')
product_link = product[1]
driver.get(product_link)
try:
    for _ in range(1):
        driver.execute_script("document.getElementsByClassName('no-underline  show-more-reviews')[0].click()")
        #time.sleep(5)
except:
    pass

soup = driver.page_source
soup = BeautifulSoup(soup)
i = soup.find_all('div',{'class':'cell-review'})

j = i[0].find_all('p')
pros = []
cons = []
overall = []

for x in range(len(j)):
    if len(j[x].findChildren('strong',recursive=False)) > 0:
        counter = 0
        if counter == 0:
            pros.append(j[x].text.split(':  ')[1])
        elif counter == 1:
            cons.append(j[x].text.split(':  ')[1])
        elif counter == 2:
            overall.append(j[x].text.split(':  ')[1])
        counter = counter + 1


j[1].text.split(':  ')


search_product('google docs')

get_reviews(('Google-Docs', 'https://www.capterra.com/p/160756/Google-Docs'))

