import requests 
from bs4 import BeautifulSoup 


URL = "http://192.168.25.1/"
page = requests.get(URL) 
soup = BeautifulSoup(page.content, 'html.parser')
soup.find_all('td')[4].get_text()