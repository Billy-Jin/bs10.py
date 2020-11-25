# 영화제목 점수 예매율, 상영시간을 추출하여 movie.csv저장 예매율 0인거 빼기
# 영화포스터는 img폴더에 저장

import requests
from bs4 import BeautifulSoup

def saveImg(imgurl,title):
    print(imgurl)
    print(title)
    title=title.replace(':','')
    title=title.replace('(','')
    title=title.replace(')','')
    title=title.replace('/','-')
    title=title.replace('?','')
    filename='img\\'+title+".jpeg"
    #filename='img\\'+title+"+imgurl[imgurl.index('?')-4:imgurl.index('?')]"
    print(filename)
    r=requests.get(imgurl)
    with open(filename,'wb') as f1:
        f1.write(r.content)
# import time
with open('data\\movie.csv','w',encoding='utf-8') as f:
        pageurl='https://movie.naver.com/movie/running/current.nhn'
        recvd=requests.get(pageurl)
        # print(recvd)
        # print(recvd.text)
        dom=BeautifulSoup(recvd.text,'lxml')
        ul=dom.find('ul',class_="lst_detail_t1")
        # print(table)
        lis=ul.find_all('li')
        print(len(lis))
        for i in range(len(lis)):                   # for li in lis
            div=lis[i].find('div',class_="thumb")
            img=div.find('img')['src'] #이미지 경로
            # print(img)
            dt1=lis[i].find('dt',class_='tit')      # li.find('dt',class_='tit')
            title=dt1.find('a').text
            title = title.replace(',',' ')
            # print(title)
            # saveImg(img,title)
            score=lis[i].find('div',class_="star_t1").find('span',class_="num").text+"점"  #find('span',class_="num") 다이렉트로 가도됨
            # print(score)
            if lis[i].find('div',class_="star_t1 b_star") and lis[i].find('div',class_="star_t1 b_star").find('span',class_="num"):
                rate=lis[i].find('div',class_="star_t1 b_star").find('span',class_="num").text+"%"
            # reserv=li.find('div',class_="star_t1 b_star") 이런식으로도 가능 첫번째 꺼  none 나오기때문에 바로 비교
            # if reserv==None:
            #        temp = ''
            # else:
            #   temp=reserv.find('span',class_="num").text
            else:
                rate=""
            # print(rate)

            ti=lis[i].find('dl',class_="info_txt1").find('span',class_="split")
            # a=lis[i].find('dl',class_="info_txt1").text
            # play=a.split('|') #[]
            # playtime=''
            # for p in play
            #     if p.count("분")==1:
            #         if p.count('개요')==1:
            #            p=p.replace('개요')
            #         playtime=p.strip()
            # print(time)

            if len(ti.next_sibling.strip())<5:
                playtime=ti.next_sibling.strip()

            else:
                time=""
            print(time)

            # print(time)
            # str='%s,%s,%s,%s%(title,score,rate,time) 도 가능
            f.write('{},{},{},{}\n'.format(title,score,rate,playtime))
            print('{},{},{}'.format(title, score,rate,playtime))
            # time.sleep(1)

