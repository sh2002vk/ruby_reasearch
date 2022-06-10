from bs4 import BeautifulSoup
import requests
import lxml
from news_links import yahoo_finance

url = yahoo_finance
response = requests.get(url)
content = BeautifulSoup(response.text, "lxml")

ran_out = False
# while
links = [content.select(f'''#Fin-Stream > ul > li:nth-child({i}) a''')[0]['href'] for i in range(11, 12)]
for link in links:
    print(f'''link: https://finance.yahoo.com/{link}''')

