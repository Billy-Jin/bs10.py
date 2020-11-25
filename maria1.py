# mariadb-10.3.27-winx64.msi
# show database;  데이터베이스목록확인
# use pythondb;   데이터베이스 선택
# show tables;    테이블목록확인

import pymysql as my
# # 1)데이터베이스 연결
# con=my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
# # 2)커서생성
# # cur=con.cursor()
# cur=con.cursor(my.cursors.DictCursor) #커서를 딕셔너리형태로 바꿈
# # 3)쿼리생성
# sql='select * from member'
# # 4)실행 처리
# cur.execute(sql)
# rows=cur.fetchall()
# for row in rows:
#     print(row)
#     print(row['no'],row['name'],row['age'],row['email'],row['birthyear'])
# # 5)자원해제
# con.close()
#-------------
# DB생성
# # 1)데이터베이스 연결
# con=my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
# # 2)커서생성
# cur=con.cursor(my.cursors.DictCursor) #커서를 딕셔너리형태로 바꿈
# # 3)쿼리생성
# while (True):
#     name=input('사용자이름=')
#     if name=="":
#         break
#     age=input('사용자 나이= ')
#     email=input('사용자 이메일= ')
#     birthyear=input('사용자 태어난연도= ')
#     sql = 'insert into member (name,age,email,birthyear) values(%s,%s,%s,%s)'
#     # 4)실행 처리
#     cur.execute(sql,(name,age,email,birthyear))
# con.commit()
#
# # 5)자원해제
# con.close()

#------------------
# # DB삭제
# # 1)데이터베이스 연결
# con=my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
# # 2)커서생성
# cur=con.cursor(my.cursors.DictCursor) #커서를 딕셔너리형태로 바꿈
# # 3)쿼리생성
# age=input('나이=')
# sql='delete from member where age<=%s'
# # 4)실행 처리
# cur.execute(sql,(age))
# con.commit()
# # 5)자원해제
# con.close()

#---------------------------
# # 이름과 태어난 년도를 입력받아 이름,나이, 태어난 년도를 수정하세요.
# # 1)데이터베이스 연결
# con=my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
# # 2)커서생성
# cur=con.cursor(my.cursors.DictCursor) #커서를 딕셔너리형태로 바꿈
# # 3)쿼리생성
# name=input('이름=')
# birthyear=input('태어난 년도=')
# sql='update member set age=%s, birthyear=%s where name=%s'
# nai=2020-int(birthyear)+1
# # 4)실행 처리
# cur.execute(sql,(nai,birthyear,name))
# con.commit()
# # 5)자원해제
# con.close()

# print('*'*30)
#------------------------
import requests
import pymysql as my
from bs4 import BeautifulSoup


con=my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
cur=con.cursor(my.cursors.DictCursor) #커서를 딕셔너리형태로 바꿈
sql='insert into movies (title,rating,reserv,playtime) values (%s,%s,%s,%s)'
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

    dt1=lis[i].find('dt',class_='tit')      # li.find('dt',class_='tit')
    title=dt1.find('a').text
    title = title.replace(',',' ')
    # print(title)
    rating=lis[i].find('div',class_="star_t1").find('span',class_="num").text+"점"  #find('span',class_="num") 다이렉트로 가도됨
    # print(score)
    if lis[i].find('div',class_="star_t1 b_star") and lis[i].find('div',class_="star_t1 b_star").find('span',class_="num"):
        reserv=lis[i].find('div',class_="star_t1 b_star").find('span',class_="num").text+"%"
    reser=lis[i].find('div',class_="star_t1 b_star") #이런식으로도 가능 첫번째 꺼  none 나오기때문에 바로 비교
    if reser==None:
           reserv = ''
    else:
      reserv=reser.find('span',class_="num").text
    # else:
    #     reserv=""
    # print(rate)

    # playtime=lis[i].find('dl',class_="info_txt1").find('span',class_="split")
    a=lis[i].find('dl',class_="info_txt1").text
    play=a.split('|') #[]
    playtime=''
    for p in play:
        if p.count("분")==1:
            if p.count('개요')==1:
               pa = p.replace('개요')
            playtime=pa.strip()
    # print(time)
    cur.execute(sql,(title,rating,reserv,playtime))
con.commit()
con.close()
