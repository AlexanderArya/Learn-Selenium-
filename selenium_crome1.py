from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument('--disable-logging')
options.add_argument('--log-level=3')  # Mengurangi level log

# Inisialisasi driver Chrome tanpa menyertakan jalur service
# Drive belum bisa di samakan dengan versi crome sementara menggunakan sleep
driver = webdriver.Chrome(options=options)

# Membuka halaman Google
driver.get("https://the-internet.herokuapp.com/login")
driver.implicitly_wait(0.5)

# Mencari element
username = driver.find_element(By.ID, 'username').send_keys("TESTING")   
password = driver.find_element(By.ID, 'password').send_keys("TESTING")
submit = driver.find_element(By.CLASS_NAME, 'radius')
submit.click()

message = driver.find_element(By.cs)

# header_text = driver.find_element(By.TAG_NAME, 'h2').text
# print("Header ditemukan:", header_text)

time.sleep(30)

driver.quit()

driver.close()
