from selenium import webdriver
from bs4 import BeautifulSoup
from warnings import filterwarnings
filterwarnings('ignore')

driver = webdriver.PhantomJS(r"E:\Warehouse\phantomjs-2.1.1-windows\bin\phantomjs.exe")

url = r'https://in.global.nba.com/players/#!/deng_adel'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
full_raw = [raw_data.get_text() for raw_data in soup.find_all('span')]
weight = full_raw[38]
dob = full_raw[54][6:16]
drafted = full_raw[54][-4:]


print(weight)
print(dob)
print(drafted)
