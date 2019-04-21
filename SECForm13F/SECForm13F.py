import pandas as pd
import numpy as np
import re
from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

import matplotlib
matplotlib.use('TkAgg')

class investmentFirm():

    def __init__(self, companyName, centralIndexKey):
        self.companyName = companyName
        self.centralIndexKey = centralIndexKey

    def getAll13Ffilings(self):

        listOfFilingDataframes = []

        accNumnbers = getAccNumbersFromCIK(self)
        filingURLs = get13FfilingURLs(self, accNumnbers)

        for filing in filingURLs:
            filingDataframe = getDataframeOfFiling(filing)
            listOfFilingDataframes.append(filingDataframe)

        return listOfFilingDataframes


    def export13FfilingsAsCSVs(self):
        dictionaryOfFilings = getDictionaryOf13Ffilings()
        placeholderNumber = 1

        for filing in listOfFilingDataframes:
            filing.to_csv('placeholder_filing_name' + placeholderNumber + '.csv')
            placeholderNumber += 1


def getAccNumbersFromCIK(self):
    url = "https://www.sec.gov/cgi-bin/browse-edgar?CIK=" + str(self.centralIndexKey) + "&action=getcompany&type=13F"

    try:
        html = urlopen(url)
        
        pageWithAllForms = BeautifulSoup(html, 'lxml')
        pageRows = pageWithAllForms.find_all('td')
        accNumbers = []

        for row in pageRows:
            rowString = str(row)
            if "<br/>Acc-no:" in rowString:
                numbersFromRow = re.findall('\d+', rowString)
                accNo = numbersFromRow[0] + numbersFromRow[1] + numbersFromRow[2]
                accNumbers.append(accNo)

        return accNumbers

    except HTTPError as err:
        print("Error for " + str(url))

def get13FfilingURLs(self, accNumbers):
    URLs = []

    for accNo in accNumbers:
        url = "https://www.sec.gov/Archives/edgar/data/" + str(self.centralIndexKey) + "/" + accNo + "/xslForm13F_X01/infotable.xml"
        URLs.append(url)

    return URLs

def getDataframeOfFiling(url):

    try:
        html = urlopen(url)
    
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

        tableOf13FFiling = pd.DataFrame(list_rows)
        tableOf13FFiling = tableOf13FFiling[0].str.split(',', expand=True)
        tableOf13FFiling[0] = tableOf13FFiling[0].str.strip('[')
        tableOf13FFiling = tableOf13FFiling.drop([0,1,2,3,4,5,6,7,8,9], axis = 0)

        return tableOf13FFiling

    except HTTPError as err:
        print("Error for " + str(url))
