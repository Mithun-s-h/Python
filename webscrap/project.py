from bs4 import BeautifulSoup
import requests

page=requests.get('https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue0')
soup=BeautifulSoup(page.text,features='html.parser')
print(soup.find_all('table',class_='wikitable sortable jquery-tablesorter'))
