from selenium import webdriver
from bs4 import BeautifulSoup
 

soup = BeautifulSoup(open('sample.html'), 'lxml')

for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        print(td.text)