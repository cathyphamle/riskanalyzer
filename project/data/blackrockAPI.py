import requests
"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

<<<<<<< HEAD
portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/performance", params= {'identifiers':"AAPL"})
# print(portfolioAnalysisRequest.text # get in text string format
performance = portfolioAnalysisRequest.json()[u'resultMap'][u'RETURNS'][0][u'performanceChart']

f = open('stock_data', 'w')
f.write(str(performance))
count = 0
for _ in performance:
    count += 1
print count
=======
portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : 'BLK~25|AAPL~25|IXN~25|MALOX~25'})
#print(portfolioAnalysisRequest.text) # get in text string format
print (portfolioAnalysisRequest.json()) # get as json object
>>>>>>> 054ea0b01a13a874938831e52f2be6cbcf5de89f
