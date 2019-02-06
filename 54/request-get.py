import requests
from time import sleep
import json

cookie = ''

headers = {
    'Cookie': 'PHPSESSID='+cookie,
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'webhacking.kr',
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15",
    'Accept-Language': 'ko-kr',
    'Referer': 'http://webhacking.kr/challenge/bonus/bonus-14/',
    'Connection': 'keep-alive',
}

for x in range(100):
    payload = {'m': x}
    res = requests.get('http://webhacking.kr/challenge/bonus/bonus-14/', params=payload, headers=headers)
    print(res.text, end='', flush=True)
    sleep(0.1)
