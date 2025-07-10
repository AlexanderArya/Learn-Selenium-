from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FS

service = FS(executable_path=r"C:\geckodriver-v0.34.0-win64\geckodriver.exe")

driver = webdriver.Firefox(service=service)

driver.get("https://www.google.com")