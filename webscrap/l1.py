# Web scraping, the process of extracting data from websites, has emerged as a powerful technique to gather information from the vast expanse of the internet.
# pip install requests
# pip install beautifulsoup4,bs4
from bs4 import BeautifulSoup
import requests

page=requests.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/')
# print(page)

soup=BeautifulSoup(page.text,features='html.parser')
# print(soup)
# print(soup.prettify()) 
# print(soup.find('div'))#finds only the first elements
# print(soup.find_all('a'))#finds all the elements
# print(soup.find_all('a',class_='gfg-stc'))#for based on attributes
# print(soup.find('div').text)#in text format
print(soup.find('div').text.strip())#in text format with cleand form






