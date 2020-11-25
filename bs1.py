#import bs4
import requests
url='https://www.naver.com'
recvd=requests.get(url)
print(recvd)       #html코드
print(recvd.text)
print(recvd.encoding)
print(recvd.headers)

from bs4 import BeautifulSoup
#bs4 안에 있는 것중에  BeautifulSoup만 출력 //대문자인 이유는 파이썬클래스이기 때문에
# 웹페이지에 접근하여 태그 인식
f=open('data\\test.html',encoding='utf-8').read()
# print(f)
# BeautifulSoup(웹페이지,파싱방식)
# 파싱:html.parser,html5lib.lxml
# dom=BeautifulSoup(f,'html.parser') # html에서 부족한 부분 채워줌 <body> 열고 안닫는것 등
dom=BeautifulSoup(f,'lxml')
# print(dom)

#특정 태그 가져오기
# dom.find('태그')    첫번째 태그 추출
# dom.태그
# div=dom.find('div')
# div=dom.div
# print(div)

# dom.find_all('태그')    모든 태그추출
# divs=dom.find_all('div')
# print(divs) #[div,div,....]
# #------------------------------
# firstdiv=dom.div
# div2=firstdiv.div
# print(div2)
# ps=div2.find_all('p')
# print(ps)
# #----------------------------
# dom.find('태그',class_='클래스명')
# dom.find('태그',{'class':'클래스명'})
# dom.find_all('class_='클래스명')
# dom.find_all('태그',{'class':'클래스명'})
# #-------------------------------------------

# cl=dom.find(class_='ex_class')
# print(cl)
# cl=dom.find('div',{'class':'ex_class'})
# print(cl)
# exs=dom.find_all({'class_':'ex_class'})
# print(exs)
# 클래스가 sister인 모든 태그
sisters=dom.find_all(class_='sister')
print(sisters)
# id가 third인 모든 태그
thirds=dom.find_all(id='third')
print(thirds)
# # id가 third인 모든 태그의 첫번째 p태그
# print(thirds[0])
# print('-'*30)
# p1=thirds[0].find('p')
# print(p1)
# a=['one']
# print(a[0])
# b='one'
# print(b)



# import , main()