# # 성탄절로 1000건 검색하여 제목과 상세내용을 blog.csv로 저장
# # items로 나눠서 각 행의 title , description찾기
#
# import os
# import sys
# import json
# import urllib.request
#
# with open('data\\blog.csv','a',encoding='utf-8') as f:
#     client_id = "e9jlWoblK1k9Moq6ynQ6"
#     client_secret = "UwnRIvG_2D"
#     encText = urllib.parse.quote("성탄절")
#
#
#     for i in range(1,1000,100):
#         url = "https://openapi.naver.com/v1/search/blog?start={}&display=100&query=" + encText # json 결과
#         # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
#         request = urllib.request.Request(url.format(i))
#         request.add_header("X-Naver-Client-Id",client_id)
#         request.add_header("X-Naver-Client-Secret",client_secret)
#         response = urllib.request.urlopen(request)
#         rescode = response.getcode()
#         if(rescode==200):
#             response_body = response.read()
#             result=response_body.decode('utf-8')
#         else:
#             print("Error Code:" + rescode)
#         dic=json.loads(result)
#
#         # print(dic['items'])
#         for k in dic['items']: #i={},{},...
#             str='{},{}\n'.format(k['title'],k['description'])
#             print(str)
#             f.write(str)
#         print(dic)

# print('*'*30)
# ---------------------------------------------------------------------------
# import os
# import sys
# import json
# import urllib.request
#
#
# client_id = "e9jlWoblK1k9Moq6ynQ6"
# client_secret = "UwnRIvG_2D"
# encText = urllib.parse.quote("가을")
#
#
# url = "https://openapi.naver.com/v1/search/movie.json?start=1&display=100&query=" + encText # json 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     result=response_body.decode('utf-8')
# else:
#     print("Error Code:" + rescode)
# dic=json.loads(result)
# print(dic)
#--------------------------------------------------------------------------# 네이버 Papago NMT API 예제
# import os
# import sys
# import urllib.request
# client_id = "_zl6nIA1_iiUxiZIlMpq"
# client_secret = "RUOxXOJmJD"
# encText = urllib.parse.quote("금요일이네요")
# data = "source=ko&target=en&text=" + encText
# url = "https://openapi.naver.com/v1/papago/n2mt"
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request, data=data.encode("utf-8"))
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)

# I have a dream을 검색하여 한국어로 변역하기
import os
import sys
import urllib.request
client_id = "_zl6nIA1_iiUxiZIlMpq"
client_secret = "RUOxXOJmJD"
with open('data\\ihd.txt','r') as f:
    encText = urllib.parse.quote(f.read())
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

#----------------------------------------------------------------------
import os
import sys
import json
import urllib.request
client_id = "_zl6nIA1_iiUxiZIlMpq"
client_secret = "RUOxXOJmJD"
with open('data\\ihd.txt','r') as f:
    encText = urllib.parse.quote(f.read())
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        a=response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)

    dic=json.loads(a)
    print(dic)
    print("*"*30)
    for i in dic["message"]:
        print(i)
        for j in i["result"]:
            print(j["translatedText"])
