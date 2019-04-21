# SECForm13F

A small tool allowing you to export SEC Form 13F from the SEC's EDGAR database as either DataFrames or .csvs.

SEC Form 13F is a quarterly report that is filed by institutional investment managers with at least $100 million in equity assets under management. It discloses their U.S. equity holdings to the Securities and Exchange Commission (SEC) and provides insights into what the smart money is doing.

The EDGAR Database can be explored [here](https://www.sec.gov/edgar/searchedgar/companysearch.html).


# How to use

To pull 13F Filings for a given company, you need the company index key, this can be found [here](https://www.sec.gov/edgar/searchedgar/companysearch.html). You should also have the company name, however this doesn't need to strictly be the official legal trading name.

In order to export 13F Filings for a company as a list of Dataframes:

``` python
import SECForm13F
testFirm = SECForm13F.investmentFirm('ARK Investment Management LLC', 1697748)
listOfFilings = testFirm.getAll13Ffilings()
```

In order to export all 13F Filings for a company as .csv files:

``` python
import SECForm13F
testFirm = SECForm13F.investmentFirm('ARK Investment Management LLC', 1697748)
testFirm.export13FfilingsAsCSVs()
```


# Updates in the pipeline
* Ability to specify number of filings
* Documents named by the dates they were filed 


I borrowed/learnt from [@joeyism](https://github.com/joeyism) and would recommend his [py-edgar](https://github.com/joeyism/py-edgar/commits?author=joeyism) repositary for exporting files as text from the SEC Database.
