# C:\Users\admin>sqlplus happy/day
# create table webtoon(
#     no number primary key,
#     title varchar2(100),
#     rating varchar2(20),
#     regdate varchar2(20)
# );
# create sequence webtoon_seq;
# insert into webtoon values (webtoon_seq.nextval,title,rating,regdate);



# import requests
# import cx_Oracle
# from bs4 import BeautifulSoup
# con=cx_Oracle.connect("scott/tiger@localhost:1521/xe")
# cur=con.cursor()
# # sql='insert into webtoon values (webtoon_seq.nextval,:1,:2,:3)'
# for page in range(1,7):
#     pageurl='https://comic.naver.com/webtoon/list.nhn?titleId=733766&page={}'.format(page)
#     recvd=requests.get(pageurl)
#     # print(recvd)
#     dom=BeautifulSoup(recvd.text,'lxml')
#     table=dom.find('table',class_="viewList")
#     # print(table)
#     trs=table.find_all('tr')
#     # print(len(trs))
#     for i in range(2,len(trs)):
#         # print(i)
#         # print(trs[i])
#         td=trs[i].find('td')
#         # print(img)
#         td1=trs[i].find('td',class_='title')
#         title=td1.find('a').text
#         div=trs[i].find('div',class_="rating_type")
#         rating=div.find('strong').text
#         # print(rating)
#         regdate=trs[i].find('td',class_="num").text
#         # cur.execute(sql,(title,rating,regdate))
# con.commit()
# con.close()

#------------------------------
import requests
import cx_Oracle
from bs4 import BeautifulSoup
con=cx_Oracle.connect("scott/tiger@localhost:1521/xe")
cur=con.cursor()
sql="insert into webtoon values (webtoon_seq.nextval,'{}','{}','{}')"
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
        # print(img)
        td1=trs[i].find('td',class_='title')
        title=td1.find('a').text
        div=trs[i].find('div',class_="rating_type")
        rating=div.find('strong').text
        # print(rating)
        regdate=trs[i].find('td',class_="num").text
        cur.execute(sql.format(title,rating,regdate))
con.commit()
con.close()