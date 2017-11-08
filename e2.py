#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup as bs

addr = 'http://historical.elections.virginia.gov/elections/download/%s/precincts_include:0/'

lines = []
for line in open("election_id.txt"):
    lines.append(line.split())

for line in lines:
    if len(line) >= 2:
        resp = requests.get(addr % (line[1]))
        with open("year" + line[0] + ".csv", "w") as csv:
            csv.write(resp.text)
