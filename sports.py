import requests
import json

with open('d:\\oraclestudy\\pj1\\data\\sports.csv','a',encoding='utf-8') as f:
    url = 'https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
    recvd = requests.get(url)
    dic=json.loads(recvd.text)
    for i in dic['list']: #i={},{},...
        str='{}::{}\n'.format(i['title'],i['subContent'])
        print(str)
        f.write(str)
#------------------------ pip install pyinstaller
#------------------------ pyinstaller sports.py
#------------------------ pyinstaller --onefile sports.py