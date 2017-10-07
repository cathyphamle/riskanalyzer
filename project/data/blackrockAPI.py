import requests

"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : 'BLK~25|AAPL~25|IXN~25|MALOX~25'})
print(portfolioAnalysisRequest.text) # get in text string format
print(portfolioAnalysisRequest.json) # get as json object