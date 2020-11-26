# class 클래스명:
#     메서드
#     메서드

# class Car:
#     def __init__(self,t,c): #생성자
#         print('생성자')
#         self.type=t
#         self.color=c
#     def showInfo(self):
#         print(self.type+','+self.color)
#     def turning(self,c):
#         self.color=c
#         self.showInfo() #다른 생성자 불러 올때도 self. 넣어줘야 에러 안생김
#     def __del__(self):
#         print('소멸자')
#
# c1=Car('suv','silver')
# # c2=Car()
# c1.showInfo() # 색상 먼저 변경하면 바뀐 색으로 나옴
# c1.turning('Black') #순서 중요

#---다중상속---------------------------------------------
# class X(object):
#     pass
# class Y:
#     pass
# class Z():
#     pass
# print('상속관계 : ',X.mro())
# print('상속관계 : ',Y.mro())
# print('상속관계 : ',Z.mro())
# class A(X,Y):
#     pass
# class B(Y,Z):
#     pass
# class D(A,B,Z):
#     pass
# class C(X,Z):
#     pass
# print('상속관계 : ',A.mro())
# print('상속관계 : ',B.mro())
# print('상속관계 : ',C.mro())
# print('상속관계 : ',D.mro())
# #너무 복잡한 다중상속은 코드 해석이 어렵다.

# class Car:
#     def __init__(self,type,color):
#         self.type=type
#         self.color=color
#         self.se=color
#     def show(self):
#         print('Car calss show 메서드',self.type,self.color)
# class KiaCar(Car):
#     def __init__(self,carname,type,color):
#         super().__init__(type,color) #부모 생성자 호출
#         self.carname = carname
#     def show(self):
#         print('KiaCar class show 메서드', self.type,self.color,self.carname)
#     def turing(self,color):
#         self.color=color
# class HyundaeCar(Car):
#     def __init__(self,carname,type,color):
#         super().__init__(type,color)    #부모생성자 호출
#         self.carname=carname
# k1=KiaCar('K9','세단','흰색')
# k1.show()
# k1.turing('노랑')
# k1.show()           #인스턴스 메서드 호출
# print(k1.carname)   #인스턴스 속성접근
# h1=HyundaeCar('제네시스','세단','비둘기색')
# h1.show()
#------------------------------------------------------
# import cx_Oracle
# class DBManager:
#     def __init__(self):
#         self.con=cx_Oracle.connect('scott/tiger@localhost:1521/xe')
#         self.cur=self.con.cursor()
#         print('연결성공')
#     def __del__(self):
#         print('연결해제')
#         self.con.close()
#     def selectAll(self):
#         sql="select * from webtoon order by no"
#         self.cur.execute(sql)
#         rows=self.cur.fetchall()
#         for row in rows:
#             print(row[0],row[1],row[2],row[3])
#             print('self.cur.description',self.cur.description)
#     def selectRating(self,rating):
#         sql="select * from webtoon where rating>{}"
#         self.cur.execute(sql.format(rating))
#         rows=self.cur.fetchall()
#         for row in rows:
#             print(row[0],row[1],row[2],row[3])
#     def insert(self,title,rating,regdate):
#         sql = "insert into webtoon values (webtoon_seq.nextval,'{}','{}','{}')"
#         self.cur.execute(sql.format(title, rating, regdate))
#         self.con.commit()
#     def updateRegdate(self,rating,regdate):
#         sql="update webtoon set regdate='{}' where rating >={}"
#         self.cur.execute(sql.format(regdate,rating))
#         self.con.commit()
#     def deleteRating(self,rating):
#         sql="delete from webtoon where rating>{}"
#         self.cur.execute(sql.format(rating))
#         self.con.commit()
# d1=DBManager()
# # d1.insert('둘리','4.999','1990.01.01')
# # d1.selectAll()
# # d1.selectRating(9.00)
# # d1.updateRegdate(9.8,'2020-12-24')
# # d1.selectRating(9.50)
# # d1.deleteRating(9.9)
# # d1.selectAll()
# color=['red','green','blue']
# fruit=['apple','orange','tomato','melon']
# number=['one','two','three','four','five']
# for t in zip(color,fruit): #가작 적은 값까지 나옴
#     print(t)
# for t in zip(color,fruit,number):
#     print(t)
# for t in zip(fruit,number):
#     print(t)
#
# for c,f,n in zip(color,fruit,number):
#     print(c,f,n)
#
#--------------------------------
import cx_Oracle
class DBManager:
    def makeDictFactory(self,cur):
        # print('self.cur.description',self.cur.description)
        # #[(컬럼명1, 데이터형, 속성1,...),(컬럼명2, 데이터형, 속성1,...),()]
        # for colinfo in self.cur.description:
        #     print(colinfo)
        #     print(colinfo[0])
        colnames=[colinfo[0]for colinfo in self.cur.description]
        # print(colnames) # ['NO', 'TITLE', 'RATING', 'REGDATE']
        # print('cur.fetchall()=',cur.fetchall())

        templist=[]
        for datas in cur.fetchall():
            print(datas)
            print(colnames)
            temp = {}
            for k,v in zip(colnames,datas):
                temp[k]=v
            print('temp=',temp)
            templist.append(temp)
        print('templist=',templist)

        # def createRow(*arg):
        #     print('createRow()함수')
        #     print(arg)
        # return createRow

    def __init__(self):
        self.con=cx_Oracle.connect('scott/tiger@localhost:1521/xe')
        self.cur=self.con.cursor()
        print('연결성공')
    def __del__(self):
        print('연결해제')
        self.con.close()
    def selectAll(self):
        sql="select * from webtoon order by no"
        self.cur.execute(sql)
        result=self.makeDictFactory(self.cur)

        for row in result:
            print(row['NO'],row['TITLE'],row['RATING'],row['REGDATE'])

    def selectRating(self,rating):
        sql="select * from webtoon where rating>={}"
        self.cur.execute(sql.format(rating))
        result=self.makeDictFactory(self.cur)
        for row in result:
            print(row['NO'],row['TITLE'],row['RATING'],row['REGDATE'])

    def insert(self,title,rating,regdate):
        sql = "insert into webtoon values (webtoon_seq.nextval,'{}','{}','{}')"
        self.cur.execute(sql.format(title, rating, regdate))
        self.con.commit()
    def updateRegdate(self,rating,regdate):
        sql="update webtoon set regdate='{}' where rating >={}"
        self.cur.execute(sql.format(regdate,rating))
        self.con.commit()
    def deleteRating(self,rating):
        sql="delete from webtoon where rating>{}"
        self.cur.execute(sql.format(rating))
        self.con.commit()
d1=DBManager()
# d1.insert('둘리','4.999','1990.01.01')
d1.selectAll()
# d1.selectRating(9.00)
# d1.updateRegdate(9.8,'2020-12-24')
# d1.selectRating(9.50)
# d1.deleteRating(9.9)
# d1.selectAll()
