from selenium import webdriver
from bs4 import BeautifulSoup
from warnings import filterwarnings
filterwarnings('ignore')

class Player():
    def __init__(self):
        self.name = ''
        self.link = ''
        self.weight = ''
        self.dob = ''
        self.drafted = ''


def get_player_names():
    
    driver = webdriver.PhantomJS(r"/media/prashant/HDD/Warehouse/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")    
    url = 'https://in.global.nba.com/playerindex/'
    driver.get(url)

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
    driver.quit()
    return players_list


def get_player_details(players_list):
    
    driver = webdriver.PhantomJS(r"/media/prashant/HDD/Warehouse/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
    
    for p in players_list:
        url = p.link

        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        full_raw = [raw_data.get_text() for raw_data in soup.find_all('span')]
        weight = full_raw[38]
        dob = full_raw[54][6:16]
        drafted = full_raw[54][-4:]

        p.weight = weight
        p.dob = dob
        p.drafted = drafted

        driver.quit()

    return players_list


player_list1 = get_player_names()
player_list = get_player_details(player_list1)