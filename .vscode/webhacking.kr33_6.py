import requests
import hashlib

#browser = 'python-requests/2.22.0'
browser = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
ip = '122.47.98.232'

b_md5 = hashlib.md5(browser.encode()).hexdigest()
ip_md5 = hashlib.md5(ip.encode()).hexdigest()

url = 'https://webhacking.kr/challenge/bonus-6/gpcc.php'
sess = requests.Session()

data = {'kk':b_md5}
cookie = {'test':ip_md5}

res = sess.post(url, data=data, cookies=cookie)
print(res.text)

