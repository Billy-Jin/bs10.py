import requests
from bs4 import BeautifulSoup
# url='https://finance.naver.com/marketindex/'
# recvd=requests.get(url)
# # print(recvd)
# # print(recvd.text)
# dom=BeautifulSoup(recvd.text,'lxml')
# span=dom.find('span',class_="value")
# print(span.text)
# print('-'*30)

# url='https://comic.naver.com/webtoon/list.nhn?titleId=733766'
# recvd=requests.get(url)
# # print(recvd)
# dom=BeautifulSoup(recvd.text,'lxml')
# table=dom.find('table',class_="viewList")
# # print(table)
# trs=table.find_all('tr')
# print(len(trs))
# for i in range(2,len(trs)):
#     # print(i)
#     # print(trs[i])
#     td1=trs[i].find('td',class_='title')
#     title=td1.find('a').text
#     div=trs[i].find('div',class_="rating_type")
#     rating=div.find('strong').text
#     # print(rating)
#     regdate=trs[i].find('td',class_="num").text
#     print('{},{},{}'.format(title,rating,regdate))

# print('-'*30)
#
# with open('data\\webtoon.csv','w',encoding='utf-8') as f:
#     url='https://comic.naver.com/webtoon/list.nhn?titleId=733766'
#     recvd=requests.get(url)
#     # print(recvd)
#     dom=BeautifulSoup(recvd.text,'lxml')
#     table=dom.find('table',class_="viewList")
#     # print(table)
#     trs=table.find_all('tr')
#     print(len(trs))
#     for i in range(2,len(trs)):
#         # print(i)
#         # print(trs[i])
#         td1=trs[i].find('td',class_='title')
#         title=td1.find('a').text
#         div=trs[i].find('div',class_="rating_type")
#         rating=div.find('strong').text
#         # print(rating)
#         regdate=trs[i].find('td',class_="num").text
#         f.write('{},{},{}\n'.format(title,rating,regdate))
# print('-'*30)
# https://comic.naver.com/webtoon/list.nhn?titleId=733766
# https://comic.naver.com/webtoon/list.nhn?titleId=733766&page=2
# https://comic.naver.com/webtoon/list.nhn?titleId=733766&page=3
# for page in range(1,7):
#     str='https://comic.naver.com/webtoon/list.nhn?titleId=733766&page={}'.format(page)
#  print(str)
# print('-'*30)
# with open('data\\webtoon.csv','w',encoding='utf-8') as f:
#     for page in range(1,7):
#         pageurl='https://comic.naver.com/webtoon/list.nhn?titleId=733766&page={}'.format(page)
#         recvd=requests.get(pageurl)
#         # print(recvd)
#         dom=BeautifulSoup(recvd.text,'lxml')
#         table=dom.find('table',class_="viewList")
#         # print(table)
#         trs=table.find_all('tr')
#         # print(len(trs))
#         for i in range(2,len(trs)):
#             # print(i)
#             # print(trs[i])
#             td1=trs[i].find('td',class_='title')
#             title=td1.find('a').text
#             div=trs[i].find('div',class_="rating_type")
#             rating=div.find('strong').text
#             # print(rating)
#             regdate=trs[i].find('td',class_="num").text
#             f.write('{},{},{}\n'.format(title,rating,regdate))
#             print('{},{},{}'.format(title, rating, regdate))

# ---------------------------------- 이미지경로, 제목, 평점, 등록일 추출
# tr안에 a안에 이미지
# import time
def saveImg(imgurl):
    print('저장중')


with open('data\\webtoon.csv','w',encoding='utf-8') as f:
    for page in range(1,7):
        pageurl='https://comic.naver.com/webtoon/list.nhn?titleId=733766&page={}'.format(page)
        recvd=requests.get(pageurl)
        # print(recvd)
        dom=BeautifulSoup(recvd.text,'lxml')
        table=dom.find('table',class_="viewList")
        # print(table)
        trs=table.find_all('tr')
        # print(len(trs))
        for i in range(2,len(trs)):
            # print(i)
            # print(trs[i])
            td=trs[i].find('td')
            img=td.find('img')['src'] #이미지 경로
            print(img)
            td1=trs[i].find('td',class_='title')
            title=td1.find('a').text
            div=trs[i].find('div',class_="rating_type")
            rating=div.find('strong').text
            # print(rating)
            regdate=trs[i].find('td',class_="num").text
            f.write('{},{},{}\n'.format(title,rating,regdate))
            print('{},{},{}'.format(title, rating, regdate))


