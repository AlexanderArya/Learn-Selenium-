from selenium import webdriver

driver = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()

driver.get('https://www.google.com/')
driver2.get('https://chatgpt.com/')
driver3.get('https://roadmap.sh/')
