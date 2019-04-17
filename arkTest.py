import pandas as pd
import numpy as np
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.sec.gov/cgi-bin/browse-edgar?CIK=0001697748&action=getcompany&type=13F"


html = urlopen(url)
pageWithAllForms = BeautifulSoup(html, 'lxml')
rows = pageWithAllForms.find_all('td')
accNumbers = []

for row in rows:
    rowString = str(row)
    #print(rowString)
    if "<br/>Acc-no:" in rowString:
        numbersFromRow = re.findall('\d+', rowString)
        accNo = numbersFromRow[0] + numbersFromRow[1] + numbersFromRow[2]
        accNumbers.append(accNo)

print(accNumbers)












def getHTMLfromURL(url):
    html = urlopen(url)
    return html

def getDataframeOfFilings(self):
    url = getURL(self)
    html = getHTMLfromURL(url)

    soup = BeautifulSoup(html, 'lxml')
    rows = soup.find_all('tr')

    for row in rows:
        row_td = row.find_all('td')

    str_cells = str(row_td)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()

    list_rows = []
    for row in rows:
        cells = row.find_all('td')
        str_cells = str(cells)
        clean = re.compile('<.*?>')
        clean2 = (re.sub(clean, '',str_cells))
        list_rows.append(clean2)

    # Data clean up
    tableOf13FFiling = pd.DataFrame(list_rows)

    # Removing commas
    tableOf13FFiling = tableOf13FFiling[0].str.split(',', expand=True)

    # Removing square brackets in first column
    tableOf13FFiling[0] = tableOf13FFiling[0].str.strip('[')

    # Removing first 10 rows
    tableOf13FFiling = tableOf13FFiling.drop([0,1,2,3,4,5,6,7,8,9], axis = 0)

    return tableOf13FFiling

def getCSVofFilings(self):
    dataframe = getDataframeOfFilings(self)
    dataframe.to_csv('13FfilingExample.csv')