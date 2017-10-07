import requests
import json
import numpy as np
import Queue
"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

def dump(js):
    print json.dumps(js, indent=2)

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : 'GOOG~20|AAPL~20|MU~20|NVDA~20|NTDOY~20', 'calculateRisk': 'true'})
jsonObject = portfolioAnalysisRequest.json()
holdings = jsonObject['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['holdings']
tickers = []
riskValues = []
myList = []
q = Queue.PriorityQueue()
for holding in holdings:
    ticker = str(holding['ticker'])
    tickers.append(ticker)

    riskData = holding['riskData']
    riskScore = riskData['totalRisk']
    risk = (ticker, riskScore)
    riskValues.append(risk)
    q.put(ticker, riskData['totalRisk'])
    myList.append(riskData['totalRisk'])


mean_duration = np.mean(myList)
std_dev_one_test = np.std(myList)
def drop_outliers(x):
    if abs(x - mean_duration) <= std_dev_one_test:
        return x
myList = filter(drop_outliers, myList)
print('Your risk score: ', np.mean(myList))
print('Your three most volatile stocks: ')
for _ in range(0, 3):
    print(q.get())