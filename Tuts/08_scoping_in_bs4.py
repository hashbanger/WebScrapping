from selenium import webdriver
from bs4 import BeautifulSoup
 
html_doc = '''
<html>
    <head>
        <title> Welcome to a fucked up tutorial</title>
    </head>
<body>
    <p class = "title">
        <b> The Me- She Story</b>
    </p>
        <p class = "story">Standing by the door with the bag on my shoulder, I look around with a lost face.
         Crap! There's no one in this room whom I think I know and damn my life for subjecting me in this situation again!!!
         I look for a place to sit and my searching sight pauses on a lone plastic stoolchair on my very right. I drag it towards me
          without a sound and take my bag off as I sit, putting it in my lap. Keeping my eyes low I try to bring my 
          nervousness under control.
          <p class = "story">..........Rest of the shit.........</p>
          </p>
        <a href = "https://www.github.com/hashbanger" id = "link1">GitHub Link</a>
        <a href = "https://www.linkedin.com" id = "link2">Linkedin Link</a>
    </p>
</body>
</html>
'''

soup = BeautifulSoup(html_doc, 'lxml')

first_p_tag = soup.find('p') # finds the first p tag , containing the title
a_tag = first_p_tag.find('a')
print(a_tag)

b_tag = first_p_tag.find('b')
print(b_tag)


