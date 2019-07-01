from selenium import webdriver
from bs4 import BeautifulSoup
from warnings import filterwarnings
filterwarnings('ignore')

# driver = webdriver.PhantomJS(r"E:\Warehouse\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver = webdriver.PhantomJS(r"/media/prashant/HDD/Warehouse/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")

url = 'https://in.global.nba.com/playerindex/'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
div = soup.find('div', class_ = 'nba-stat-table')

names_list = []
for a in div.find_all('a'):
    for num,sp in enumerate(a.find_all('span')):

        if num % 2 ==0:
            f_name = ''
        f_name += ' '+str(sp.text)
        if num % 2 !=0:
            names_list.append(str.lstrip(f_name))

print(names_list)
driver.quit()
        