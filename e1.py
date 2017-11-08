#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

r = requests.get("http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General")
soup = bs(r.content, 'html.parser')

tr = soup.find_all('tr', 'election_item')

for t in tr:
    id = t['id'][-5:]
    year = t.td.text
    print(year, id, file = open('election_id.txt', 'a'))
