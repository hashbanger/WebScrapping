from selenium import webdriver
from bs4 import BeautifulSoup
from warnings import filterwarnings
filterwarnings('ignore')

driver = webdriver.PhantomJS(r"E:\Warehouse\phantomjs-2.1.1-windows\bin\phantomjs.exe")
url = 'https://in.global.nba.com/playerindex/'
driver.get(url)

class Player():
    def __init__(self):
        self.name = ''
        self.link = ''


soup = BeautifulSoup(driver.page_source, 'lxml')
div = soup.find('div', class_ = 'nba-stat-table')

players_list = []
for a in div.find_all('a'):
    for num,sp in enumerate(a.find_all('span')):

        if num % 2 ==0:
            f_name = ''
        f_name += ' '+str(sp.text)
        if num % 2 !=0:
            player = Player()
            player.name = str.lstrip(f_name)
            player.link = 'https://in.global.nba.com'+ a['href']
            players_list.append(player)

for player in players_list:
    print(player.name)
    print(player.link)
    print()
driver.quit()
        