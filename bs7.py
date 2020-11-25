# import requests
# import json

# with open('data\\sport.csv','w',encoding='utf-8') as f:
#     # url='https://sports.news.naver.com/wfootball/news/index.nhn?isphoto=N'
#     url = 'https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
#     recvd = requests.get(url)
#
#
#
#     dic=json.loads(recvd.text)
#     # print(dic)
#     # print(dic['list']) #[{},{},{},...]
#     # 기사제목, 내용을 출력
#     for i in dic['list']: #i={},{},...
#         str='{}::{}\n'.format(i['title'],i['subContent'])
#         print(str)
#         f.write(str)

#-----------------------------------------------------------------
# import requests
# from fake_useragent import UserAgent
# import json

# url='https://finance.daum.net'

# ua=UserAgent() # UserAgent ua=new UserAgent()
# # print(ua.chrome)
# # print(ua.ie)
# with open('data\\money.csv','w',encoding='utf-8') as f:
#     headers={'user-agent':ua.chrome,'referer':'https://finance.daum.net/'}
#     url='https://finance.daum.net/api/search/ranks?limit=10'
#     recvd = requests.get(url,headers=headers)
#     # print(recvd)
#     # print(recvd.text)
#     dic=json.loads(recvd.text)
#     # print(dic)
#     print(dic['data'])
#     for i in dic['data']: #i={},{},...
#         str='{},{},{}\n'.format(i['rank'],i['name'],i['changePrice'])
#         print(str)
#         f.write(str)

#--------------------------------------------------------------
# 성탄절로 1000건 검색하여 제목과 상세내용을 blog.csv로 저장
# items로 나눠서 각 행의 title , description찾기

import os
import sys
import json
import urllib.request

with open('data\\blog.csv','w',encoding='utf-8') as f:
    client_id = "e9jlWoblK1k9Moq6ynQ6"
    client_secret = "UwnRIvG_2D"
    encText = urllib.parse.quote("성탄절")


    for i in range(1,901,100):
        url = "https://openapi.naver.com/v1/search/blog?start="+str(i)+"&display=100&query=" + encText # json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result=response_body.decode('utf-8')
        else:
            print("Error Code:" + rescode)
        dic=json.loads(result)

        # print(dic['items'])
        for k in dic['items']: #i={},{},...
            str='{},{}'.format(k['title'],k['description'])
            print(str)
            f.write(str)
        print(dic)
