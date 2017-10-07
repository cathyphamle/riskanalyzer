import requests
import json
"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : 'IBM~34|BLK~33|AAPL~33', 'calculateRisk': 'true'})
jsonObject = portfolioAnalysisRequest.json()
#print json.dumps(jsonObject['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['riskData'], indent=2)
print json.dumps(jsonObject['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['riskData']['riskFactorsMap'], indent=2)
portfolios = jsonObject['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['holdings']
tickers = []
"""for holding in portfolios:
    tickers.append(str(holding['ticker']))
    #print json.dumps(holding, indent=2)
"""
#print 'TICKERS: ', tickers
#print json.dumps(portfolios, indent=4) # get in text string format
#portfolioAnalysisRequest.json # get as json object