from selenium import webdriver
from bs4 import BeautifulSoup
from warnings import filterwarnings

filterwarnings('ignore')

driver = webdriver.PhantomJS(executable_path = r"E:\Warehouse\phantomjs-2.1.1-windows\bin\phantomjs.exe")
# Phantom JS has been deprecated use 'headless'
driver.get('https://python.org')

html_doc = driver.page_source

soup = BeautifulSoup(html_doc, 'lxml')

first_p_tag = soup.find('p')
all_a_tags = soup.find_all('a')

print("First p tag")
print(first_p_tag)
print("\nAll a tag")
print(all_a_tags)

