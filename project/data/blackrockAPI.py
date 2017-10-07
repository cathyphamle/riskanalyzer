
import requests
import json
<<<<<<< HEAD
import numpy as np
import Queue

def dump(js):
    print json.dumps(js, indent=2)

def setParams(tickers):
    positions = ''
    distNum = 100 / len(tickers)
    currTotal = 0
    for i in range(0, len(tickers)):
        positions = positions + tickers[i] + '~'
        if i != len(tickers) - 1:
            positions += str(distNum) + '|'
            currTotal += distNum
        else:
            positions += str(100 - currTotal)
    return positions

def getRiskScore(ticker):
    return

def getRecommendations(score):
    with open('tickers.txt', 'r') as fin:
        for line in fin:
            param = line.strip() + '~100'
            portfolioJson = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis",
                                                    params={'positions': param, 'calculateRisk': 'true'}).json()
            holding = portfolioJson['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['holdings'][0]
            if 'riskData' in holding:
                riskData = holding['riskData']
                if 'riskTotal' in riskData:
                    print riskData['riskTotal']

            print score

        # Do string processing here

def main(tickers):
    portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : setParams(tickers), 'calculateRisk': 'true'})
    performanceDataRequest = requests.get("https://www.blackrock.com/tools/hackathon/performance", params= {'identifiers':tickers, 'includePositionReturns':'true'})
    portfolioJson = portfolioAnalysisRequest.json()
    performanceJson = performanceDataRequest.json()
    holdings = portfolioJson['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['holdings']
    performance = performanceJson['resultMap']['RETURNS']
    tickers = []
    myList = []
    q = Queue.PriorityQueue()
    for holding in holdings:
        ticker = str(holding['ticker'])
        tickers.append(ticker)
        score = holding['riskData']['totalRisk']
        q.put(ticker, score)
        myList.append(score)
    mean_duration = np.mean(myList)
    std_dev_one_test = np.std(myList)
    def drop_outliers(x):
        if abs(x - mean_duration) <= 2 * std_dev_one_test:
            return x
    myList = filter(drop_outliers, myList)
    riskScore = np.mean(myList)
    print('Your risk score: ', riskScore)
    print('Your three most volatile stocks: ')
    for _ in range(0, 3):
        if not q.empty():
            print(q.get())

    for result in performance:
        performanceChart = result['performanceChart']

    getRecommendations(riskScore)

if __name__ == "__main__":
    params = ['MU', 'NVDA', 'SQM','AAPL', 'GOOG', 'DATA']
    main(params)
