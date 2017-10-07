import requests
"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/performance", params= {'identifiers':"AAPL"})
# print(portfolioAnalysisRequest.text # get in text string format
performance = portfolioAnalysisRequest.json()[u'resultMap'][u'RETURNS'][0][u'performanceChart']

f = open('stock_data', 'w')
f.write(str(performance))
count = 0
for _ in performance:
    count += 1
print count