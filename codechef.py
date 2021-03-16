import requests
from bs4 import BeautifulSoup

url = 'https://clist.by/api/v1/json/contest/?&order_by=-start&username=swiggy123&api_key=a0fc6e7ce627ee61b7fced4c976609b97bb65b76'
params = dict({
    'resource__id': 2
})
resp = requests.get(url=url, params=params)
x = resp.json()
t = x['objects']
for i in t:
    print(i['event'])
