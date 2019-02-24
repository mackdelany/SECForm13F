### Test scrap of SEC Ark Investment Page
### Example URL:
### https://www.sec.gov/Archives/edgar/data/1697748/000114420418057760/xslForm13F_X01/infotable.xml

# Importing packages
import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import seaborn as sns
#%matplotlib inline

# Importing URL request and BeautifulSoup functions
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Setting Ark link as URL / html value
url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001697748&type=13F-HR&dateb=&owner=exclude&count=100"
html = urlopen(url)

# Passing URL to BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
type(soup)

# Checking the text
rows = soup.find_all('tr')

# Taking table rows into list form
for row in rows:
    row_td = row.find_all('td')

# Removing HTML tags
str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()


# finding all the characters inside the < td > html tags and replace them with an empty string for each table row
import re

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
type(clean2)

# Data clean up
df = pd.DataFrame(list_rows)

# Removing commas
df1 = df[0].str.split(',', expand=True)

# Removing square brackets in first column
df1[0] = df1[0].str.strip('[')

# Removing first 10 rows
###df2 = df1.last.

## Need to work out how to remove last rows go back to https://www.datacamp.com/community/tutorials/web-scraping-using-python

print(df1)
