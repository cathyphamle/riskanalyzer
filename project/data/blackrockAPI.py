import requests
import json
import numpy as np
import Queue
import time
import csv
from sqlite3 import dbapi2 as sqlite

def dump(js):
    print json.dumps(js, indent=2)

def create_connection(path):
	con = sqlite3.connect(path)
	df = pd.read_sql_query("SELECT * from Blackrock", con)
	return df

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
    bestSoFar = (float('inf'), '')
    tickers = []
    i = 0
    with open('companylist.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tickers.append(row['Symbol'])
            sector = row['Sector']
    start = time.clock()
    while len(tickers) > 0:
        params = tickers[0:10]
        tickers = tickers[10:]
        performanceData = requests.get("https://www.blackrock.com/tools/hackathon/performance", params= {'identifiers':tickers, 'includePositionReturns':'true'})
        performance = performanceJson['resultMap']
        if 'RETURNS' in performance:
            returns = performance['RETURNS']
            for info in returns:
                current_time = time.clock()
                elapsed = current_time - start
                #print("speed: ", round(i / elapsed, 1), " requests/second")
                i+= 1
                if 'ticker' in info and 'latestPerf' in info:
                    perf = info['latestPerf']
                    if 'oneYearSharpeRatio' in perf:
                        currScore = perf['oneYearSharpeRatio']
                        closeness = abs(score - currScore)
                        if closeness < bestSoFar[0]:
                            bestSoFar = (closeness, info['ticker'])
    return bestSoFar[1]


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
    for result in performance:
        info = result['latestPerf']
        ticker = result['ticker']
        dump(result)
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
    for _ in range(3):
        if not q.empty():
            print q.get()
    getRecommendations(riskScore)

    create_connection('/Users/Cathy/blackrock.db')

if __name__ == "__main__":
    params = ['MU', 'NVDA', 'SQM','AAPL', 'GOOG', 'DATA']
    main(params)
