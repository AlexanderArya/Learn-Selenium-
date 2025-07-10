import requests
from bs4 import BeautifulSoup

# Mengambil konten HTML dari halaman web
response = requests.get('https://the-internet.herokuapp.com/login')

# Mem-parsing konten HTML menggunakan BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
# Menemukan elemen dengan tag 'h1'
header = soup.find(class_='subheader')

if header:  
    print(header.text)
else:
    print("Tidak ada")

# Mencetak teks dari elemen tersebut