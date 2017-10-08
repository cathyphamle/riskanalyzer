import requests
import json
import numpy as np
import Queue
import time
import csv

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

def getRecommendations(holdingTicker, score):
    tickers = []
    i = 0
    with open('tickerToRisk.csv', mode='r') as infile:
        reader = csv.reader(infile)
        riskDict = dict((rows[0],rows[1]) for rows in reader)
        tickers = riskDict.keys()
    with open('tickerToSharpe.csv', mode='r') as infile:
        reader = csv.reader(infile)
        sharpeDict = dict((rows[0],rows[1]) for rows in reader)
    for ticker in tickers:
    top = []

    best = (holdingTicker, sharpeDict[holdingTicker])
    for _ in range(20):
        top.append(q.get())
    for potentialRecommendation in top:
        print potentialRecommendation
        currSharpeScore = sharpeDict[ticker]
        if currSharpeScore >= best[1]:
            best = (ticker, currSharpeScore)
    return best


def main(tickers):
    #portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : setParams(tickers), 'calculateRisk': 'true'})
    performanceDataRequest = requests.get("https://www.blackrock.com/tools/hackathon/performance", params= {'identifiers':tickers, 'includePositionReturns':'true'})
    #portfolioJson = portfolioAnalysisRequest.json()
    performanceJson = performanceDataRequest.json()
    performance = performanceJson['resultMap']['RETURNS']
    tickers = []
    q = Queue.PriorityQueue()
    def drop_outliers(x):
        if abs(x - mean_duration) <= 2 * std_dev_one_test:
            return x
    myList = []
    recommendations = []
    for result in performance:
        info = result['latestPerf']
        ticker = result['ticker']
        if 'oneYearSharpeRatio' in info and 'oneYearRisk' in info:
            sharpescore = info['oneYearSharpeRatio']
            myList.append(sharpescore)
            score = info['oneYearRisk']
            q.put(ticker, score)
            tickers.append(ticker)
    mean_duration = np.mean(myList)
    std_dev_one_test = np.std(myList)
    myList = filter(drop_outliers, myList)
    riskScore = np.mean(myList)
    print 'Your risk score: ', str(riskScore)
    print('Your three most volatile stocks: ')
    toReplace = []
    for _ in range(3):
        if not q.empty():
            i = q.get()
            print i
            toReplace.append(i)
    for ticker in toReplace:
        recommendations.append((ticker, getRecommendations(ticker, score)))
    print recommendations

if __name__ == "__main__":
    params = ['MU', 'NVDA', 'SQM','AAPL']
    main(params)
