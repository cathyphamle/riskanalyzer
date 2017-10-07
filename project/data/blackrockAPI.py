import requests
import json
"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : 'IBM~20|BLK~20|AAPL~20|IXN~20|MALOX~20'})
jsonObject = portfolioAnalysisRequest.json()
portfolios = jsonObject['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['holdings']
for holding in portfolios:
    print holding['returnOnAssets']
#print json.dumps(portfolios, indent=4) # get in text string format
#portfolioAnalysisRequest.json # get as json object