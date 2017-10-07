import requests
import json
import numpy as np
"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

def dump(js):
    print json.dumps(js, indent=2)

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : 'SQM~50|AAPL~50', 'calculateRisk': 'true'})
jsonObject = portfolioAnalysisRequest.json()
holdings = jsonObject['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['holdings']
tickers = []
riskValues = []
myList = []
for holding in holdings:
    ticker = str(holding['ticker'])
    tickers.append(ticker)
    riskData = holding['riskData']
    risk = (ticker, riskData['totalRisk'])
    riskValues.append(risk)
    myList.append(riskData['totalRisk'])

mean_duration = np.mean(myList)
std_dev_one_test = np.std(myList)
def drop_outliers(x):
    if abs(x - mean_duration) <= std_dev_one_test:
        return x
myList = filter(drop_outliers, myList)
print('Your risk score: ', np.mean(myList))

#print 'TICKERS: ', tickers