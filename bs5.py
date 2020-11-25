import requests
from bs4 import BeautifulSoup

# 이미지경로, 제목, 평점, 등록일 추출
def saveImg(imgurl,title):
    print(imgurl)
    print(imgurl[-4:])
    print(title)
    title=title.replace(': ','')
    title=title.replace('(','')
    title=title.replace(')','')
    title=title.replace('/','-')
    title=title.replace('?','')
    filename='img\\'+title+imgurl[-4:]
    print(filename)
    r=requests.get(imgurl)
    with open(filename,'wb') as f1:
        f1.write(r.content)
import time
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
            # print(img)
            td1=trs[i].find('td',class_='title')
            title=td1.find('a').text
            saveImg(img,title)
            div=trs[i].find('div',class_="rating_type")
            rating=div.find('strong').text
            # print(rating)
            regdate=trs[i].find('td',class_="num").text
            f.write('{},{},{}\n'.format(title,rating,regdate))
            print('{},{},{}'.format(title, rating, regdate))
            time.sleep(1)
# 모든 페이지의 이미지를 다운로드하고, 제목, 평점, 등록일을 webtoon.csv파일로 저장