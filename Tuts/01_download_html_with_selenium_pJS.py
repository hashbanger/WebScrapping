from selenium import webdriver

#driver = webdriver.Chrome(executable_path = r"E:\Warehouse\chromedriver.exe")

driver = webdriver.PhantomJS(executable_path = r"E:\Warehouse\phantomjs-2.1.1-windows\bin\phantomjs.exe")

driver.get('https://python.org')

html_doc = driver.page_source

print(html_doc)