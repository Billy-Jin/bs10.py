

# import sqlite3

#프롬프트 모양이 sqlite>로 변경됨
#
# .open 데이터베이스이름 : 사용할 데이터베이스 지정
# .open pythondb
# .table
# create table member(
# id char(4),
# name char(20),
# age int,
# email char(30),
# birthyear int
# );
# table
# .schema 테이블이름 : 테이블의 구조 확인
# insert into member values('aaa','kim',20,'aaa@naver.com',2001);
# insert into member values('bbb','l22',25,'bbb@naver.com',1996);
# select * from member;
# .header on : select 사용시 헤더 보여줌
# select * from member;
# .mode column : select 사용시 컬럼모드로 출력
# select * from member;
# .quit
# ------재접속시
# sqlite3
# .open pythondb
# .table

# import sqlite3
# # 1)데이터베이스 연결
# con=sqlite3.connect("d:\sqlite\pythondb")
# # 2)커서생성
# cur=con.cursor()
# # 3)쿼리생성
# sql="select * from member"
# # 4)실행 처리
# cur.execute(sql)
# while(True):
#     row=cur.fetchone() #fetchone() 한줄에 접근
#     if row==None:
#         break
#     # print(row)
#     print(row[0],row[1],row[2],row[3],row[4])
# # 5)자원해제
# con.close()
# print('*'*30)
# -------------------------------------------------

# import sqlite3
# # 1)데이터베이스 연결
# con=sqlite3.connect("d:\sqlite\pythondb")
# while (True):
#     id=input('사용자 id= ')
#     if id=="":
#         break
#     name=input('사용자 이름= ')
#     age=input('사용자 나이= ')
#     email=input('사용자 이메일= ')
#     birthyear=input('사용자 태어난연도= ')
#  # 2)커서생성
#     cur=con.cursor()
#     # 3)쿼리생성
#     # insert into member values (id,name,age,email,birthyear)
#     sql="insert into member values('"+id+"','"+name+"','"+age+"','"+email+"','"+birthyear+"')"
#     # 4)실행 및 처리
#     cur.execute(sql)
#     con.commit()
# # 5)자원해제
# con.close()

# print('*'*30)
#-------------------------------------------------------------------

import sqlite3
# 1)데이터베이스 연결
con=sqlite3.connect("d:\sqlite\pythondb")
# 2)커서생성
cur=con.cursor()
# 3)쿼리생성

sql="delete from member"
# 4)실행 및 처리
cur.execute(sql)
con.commit()
# 5)자원해제
con.close()
