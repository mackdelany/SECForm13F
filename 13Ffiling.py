### Example scrap of a 13F Ark Investment Page
### Example URL:
### https://www.sec.gov/Archives/edgar/data/1697748/000114420418057760/xslForm13F_X01/infotable.xml

# Importing packages
import pandas as pd
import numpy as np
import re
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

# Importing URL request and BeautifulSoup functions
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Set URL, will use Ark link as example
url = "https://www.sec.gov/Archives/edgar/data/1697748/000114420418057760/xslForm13F_X01/infotable.xml"
html = urlopen(url)

# Passing URL to BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
type(soup)

# Checking the text
rows = soup.find_all('tr')

# Taking table rows into list 
for row in rows:
    row_td = row.find_all('td')

# Removing HTML tags
str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()

# Finding all characters inside <td> html tags and replacing
# them with an empty string for each table row

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
type(clean2)

# Data clean up
tableOf13FFiling = pd.DataFrame(list_rows)

# Removing commas
tableOf13FFiling = tableOf13FFiling[0].str.split(',', expand=True)

# Removing square brackets in first column
tableOf13FFiling[0] = tableOf13FFiling[0].str.strip('[')

# Removing first 10 rows
tableOf13FFiling = tableOf13FFiling.drop([0,1,2,3,4,5,6,7,8,9], axis = 0)
tableOf13FFiling.to_csv('13FfilingExample.csv')

print(tableOf13FFiling)
