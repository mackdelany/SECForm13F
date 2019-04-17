### Example scrap of a 13F Ark Investment Page
### Example URL:
### https://www.sec.gov/Archives/edgar/data/1697748/000114420418057760/xslForm13F_X01/infotable.xml

# Importing packages
import pandas as pd
import numpy as np
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

class investmentFirm():

    def __init__(self, companyName, centralIndexKey):
        self.companyName = companyName
        self.centralIndexKey = centralIndexKey

    def getURL(self):
        url = "https://www.sec.gov/Archives/edgar/data/" + self.cik + "/000114420418057760/xslForm13F_X01/infotable.xml"
        return url

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




## TEST
## ARK CIK: 1697748
