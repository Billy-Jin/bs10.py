# import requests
# import cx_Oracle
# from bs4 import BeautifulSoup
# # S_PAGENUMBER: 3
# # S_MB_CD: 10012941
# # S_HNAB_GBN: I
# # hanmb_nm: 전소연
# # sort_field: SORT_PBCTN_DAY
#
# # create table writing(
# #     no number primary key,
# #     title varchar2(100),
# #     singer varchar2(100),
# #     write varchar2(100)
# # );
# # create sequence writing_seq;
#
# #  ALTER TABLE writing MODIFY(write VARCHAR2(300));
#
# con=cx_Oracle.connect("scott/tiger@localhost:1521/xe")
# cur=con.cursor()
# sql="insert into writing values (writing_seq.nextval,'{}','{}','{}')"
# url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
# data={'S_PAGENUMBER': 1,
# 'S_MB_CD': '10012941',
# 'S_HNAB_GBN': 'I',
# 'hanmb_nm': '전소연',
# 'sort_field': 'SORT_PBCTN_DAY'}
# recvd=requests.post(url,data=data)
# # print(recvd)
# dom = BeautifulSoup(recvd.text, 'lxml')
# div = dom.find_all('div',class_="board col")
# div1=div[1]
# tb = div1.find('tbody')
# trs = tb.find_all('tr')
# # print(trs)
# for i in range(len(trs)):
#     # td = trs[i].find_all('td')
#     title = trs[i].find_all('td')[0].text
#     singer = trs[i].find_all('td')[1].text
#     write = trs[i].find_all('td')[2].text
#     # print(len(td))
#     # for j in range(len(td)):
#     #     title=td[0].text
#     #     singer=td[1].text
#     #     write=td[2].text
#     print(title+" / "+singer+" / "+write)
#     # cur.execute(sql.format(title, singer, write))
# # con.commit()
# # con.close()
# # 저작물명,가수명,작사를 오라클에 저장하세요

#---------------------------------------------------------------

import requests
import cx_Oracle
from bs4 import BeautifulSoup
# S_PAGENUMBER: 3
# S_MB_CD: 10012941
# S_HNAB_GBN: I
# hanmb_nm: 전소연
# sort_field: SORT_PBCTN_DAY

# create table writing(
#     no number primary key,
#     title varchar2(100),
#     singer varchar2(100),
#     write varchar2(100)
# );
# create sequence writing_seq;

#  ALTER TABLE writing MODIFY(write VARCHAR2(300));

# con=cx_Oracle.connect("scott/tiger@localhost:1521/xe")
# cur=con.cursor()
# sql="insert into writing values (writing_seq.nextval,'{}','{}','{}')"
# url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
# for k in range(1,5):
#     data={'S_PAGENUMBER': k,
#     'S_MB_CD': '10012941',
#     'S_HNAB_GBN': 'I',
#     'hanmb_nm': '전소연',
#     'sort_field': 'SORT_PBCTN_DAY'}
#     recvd=requests.post(url,data=data)
#     # print(recvd)
#     dom = BeautifulSoup(recvd.text, 'lxml')
#     div = dom.find_all('div',class_="board col")
#     div1=div[1]
#     tb = div1.find('tbody')
#     trs = tb.find_all('tr')
#     # print(trs)
#     for i in range(len(trs)):
#         # td = trs[i].find_all('td')
#         title = trs[i].find_all('td')[0].text
#         singer = trs[i].find_all('td')[1].text
#         write = trs[i].find_all('td')[2].text
#         # print(len(td))
#         # for j in range(len(td)):
#         #     title=td[0].text
#         #     singer=td[1].text
#         #     write=td[2].text
#         print(title+" / "+singer+" / "+write)
#         cur.execute(sql.format(title, singer, write))
# # con.commit()
# # con.close()
# # 저작물명,가수명,작사를 오라클에 저장하세요


#------------------------------------------------------------------------
# import requests
# import cx_Oracle
# from bs4 import BeautifulSoup
# # S_PAGENUMBER: 3
# # S_MB_CD: 10012941
# # S_HNAB_GBN: I
# # hanmb_nm: 전소연
# # sort_field: SORT_PBCTN_DAY
#
# # create table music(
# #     no number primary key,
# #     title varchar2(300),
# #     singer varchar2(300),
# #     song varchar2(300)
# # );
# # create sequence music_seq;
#
# #  ALTER TABLE writing MODIFY(write VARCHAR2(300));
#
# con=cx_Oracle.connect("scott/tiger@localhost:1521/xe")
# cur=con.cursor()
# sql="insert into music values (music_seq.nextval,'{}','{}','{}')"
# url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
# for page in range(1,7):
#     data={'S_PAGENUMBER': page,
#     'S_MB_CD': '10001319',
#     'S_HNAB_GBN': 'I',
#     'hanmb_nm': '정진영',
#     'sort_field': 'SORT_PBCTN_DAY'}
#     recvd=requests.post(url,data=data)
#     # print(recvd)
#     dom = BeautifulSoup(recvd.text, 'lxml') # 파싱을 거쳐서 태그 인식
#     tables = dom.find_all('table')
#     # print(len(tables)) #2
#     trs=tables[1].find_all('tr')
#     # print(len(trs)) #11
#     for i in range(1,len(trs)):
#         tds = trs[i].find_all('td')
#         # print(tds)
#         title = tds[0].text
#         singer = tds[1].text
#         song = tds[2].text
#         print(title+" / "+singer+" / "+song)
#         title=title.replace("'",' ')
#         cur.execute(sql.format(title, singer, song))
# con.commit()
# con.close()
# # 저작물명,가수명,작사를 오라클에 저장하세요

#-----------------------------------------------------------------------------
# import requests
# from bs4 import BeautifulSoup
# with open('data\\kma.csv','w',encoding='utf-8') as f:
#     url='https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
#     recvd=requests.get(url)
#     # print(recvd.text)
#     # print(recvd)
#     #서울ㆍ인천ㆍ경기도 기상데이터
#     dom=BeautifulSoup(recvd.text,'lxml')
#     locations=dom.find_all('location')
#     # print(len(locations))
#     for location in locations:
#         province=location.find('province').text
#         city=location.find('city').text
#         # print(province,city)
#         datas=location.find_all('data')
#         for data in datas:
#             mode=data.find('mode').text
#             tmEf=data.find('tmef').text #대문자되어있어도 소문자로 사용해야만 값이 나옴
#             wf=data.find('wf').text
#             tmn=data.find('tmn').text
#             tmx=data.find('tmx').text
#             reliability=data.find('reliablity')
#             rnSt=data.find('rnst').text
#             str='{},{},{},{},{},{},{},{},{}\n'.format(province,city,mode,tmEf,wf,tmn,tmx,reliability,rnSt)
#             # print(str)
#             f.write(str)

#---------------------------------------
import re #정규표현식

# str='''3412    Bob 123
# 3834  Jonny 333
# 1248   Kate 634
# 1423   Tony 567
# 2567  Peter 435
# 3567  Alice 535
# 1548  Kerry 534'''
#
# #re.findall(r'패턴',문자열)
# r1=re.findall('[0-9]',str)
# print(r1)
# r2=re.findall(r'[0-9]+',str) #+넣으면 붙어있는것 나옴
# print(r2)
# r1=re.findall(r'[A-Z]+',str)
# print(r1)

#--------------
# * 0번이상
# + 1번이상,
# ? 0또는 1
# | (선택)
# . 줄바꿈을 제외한 한글자
# [],{1,3} 1번이상 3번미만, {,3} 3번 미만 ,{1,}1번이상 {3} 3번
# 옵션
# re.IGNORECASE(I) : 대소문자 구분X
# re.DOTALL(S) : 줄바꿈 포함
# re.VERBOSE(X) : 정규식에 주석을 사용할수 있다

# print(re.match('a.b','aabrrr'))
# print(re.match('a.b','a0brrr'))
# print(re.match('a.b','c0brrr'))
# print(re.findall('a.b','a0brrr'))
# print(re.search('a.b','aabrrr'))
# str='3pink dress'
# print(re.match('[a-z]+',str))   # 문자열 처음부터 정규식과 일치여부
# print(re.search('[a-z]+',str))  # 문자열 전체르 검색하여 일치여부
# # group()정규식에 일치하는 문자열 추출
# # print(re.findall('[a-z]+',str)) # 정규식에 일치하는 문자열 반환
# print(re.match('[a-z]+',str).group()) # 문자열 전체를 검색하여 일치여부
# print(re.search('[a-z]+',str).group()) # 문자열 전체를 검색하여 일치여부
# str='pink333 dress444'
# print(re.match('[a-z]+',str).group())
# print(re.search('[a-z]+',str).group())
# print(re.findall('[a-z]',str))

# str='My handphone number 010-3333-7890'
# print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d',str))
# print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d',str).group())
# print(re.search('[0-9]{3,4}-[0-9]{3,4}-[0-9]{3,4}',str).group())
# print(re.match('\d\d\d-\d\d\d\d-\d\d\d\d',str).group())
# print(re.findall('\d\d\d-\d\d\d\d-\d\d\d\d',str))

# str='''3412    Bob 123
# 3834  Jonny 333
# 1248   Kate 634
# 1423   Tony 567
# 2567  Peter 435
# 3567  Alice 535
# 1548  Kerry 534'''
#
# print(re.findall('[a-z]+',str,re.I))
# t1=re.compile('[a-z]+')
# print(t1.findall(str,re.I))


#--------------------------------------------------------
# import pyperclip
#
# # pyperclip.copy('한글도 되나?!')
# print(pyperclip.paste())
# # ngmo2@naver.com
# email_regex=re.compile(r'''(
#     [a-zA-z0-9_.-]+     #sername
#     @                   #@ 기호
#     [a-zA-z0-9_.-]+     #도메인
#     (\.[a-zA-Z]{2,4}){1,2}  #dot 등등
#     )''', re.VERBOSE)
# text=pyperclip.paste()
# result=email_regex.findall(text)
# print(result)
# for r in result:
#     print(r[0])

f=text=open('data\\test.html',encoding='utf-8')
text=f.read()
# print(text)
# tag=re.compile('<.+>') #탐욕적 방식
tag=re.compile('<.+?>') #게으른방식
print(tag.match(text))
print(tag.search(text))
print(tag.findall(text))
print('-'*30)
tag=re.compile('<(.+?)>') #게으른방식
print(tag.findall(text))

#i로 시작하고 n으로 끝나는 모든 문자
str='internationalization'
test=re.compile(r'i.+n') #탐욕적 방식 전체 다 나옴
print(test.findall(str))
test=re.compile(r'i.+?n') #게으른 방식 개별로 나옴
print(test.findall(str))


# 치환

# 클래스

# 정규식