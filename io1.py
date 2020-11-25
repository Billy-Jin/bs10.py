#변수=open('파일명',모드) # 안줄시 기본모드는 읽기
#사용
#변수.close()     자원반납
# 모드 : r(읽기),w(쓰기),a(추가)
# f=open('d:\oraclestudy\pj1\data\poem.txt',encoding='utf-8')
# #txt=f.read() #전체내용읽기
# txt=f.read(5) #5글자 읽기
# print(txt)
# print(type(txt))
# f.close()
# print('\n\n\n\n\n\n\n')

# f=open('data\\poem.txt',encoding='utf-8')
# txt=f.readline()    #한 줄 읽기
# print(txt)
# print(type(txt))    #문자열
# f.close()

# f=open('data\\poem.txt',encoding='utf-8')
# txt=f.readlines()    #줄단위 리스트 반환
# print(txt)
# print(type(txt))    #문자열
# for line in txt:
#     print(line.strip())
# f.close()
#

# with oppen('파일명',모드)as 변수명:
# with블럭이 끝날때 자동 close
# with open('data\\poem.txt',encoding='utf-8') as f:
#     txt=f.read()
#     print(txt)
# with open('data\\test1.txt','w',encoding='utf-8') as f:
#     f.write('very nice day!!\n')
#     f.write('이렇게 좋은날~')

# with open('data\\test2.txt',mode='a',encoding='utf-8')as f: #a=append로 마지막 들 뒤에 이어붙이기 함
#     for i in range(100):
#         f.write(str(i)+'\n')

# fruit=['사과','배','포도']
# with open('data\\test2.txt','a',encoding='utf8') as f:
#     # for a in fruit:
#     #     f.write(a)
#     f.writelines(fruit) #리스트를 파일에 쓰기 / 위 두줄과 동일

# with open('data\\test1.txt','w') as f:
#     print('test print',file=f)

# col=['이름','나이','주소']
# names=['홍길동','심청','이몽룡','성춘향']
# age=[20,16,16,16]
# juso=['서울','서산','남원','진주']
# with open('data\\addr.txt','w',encoding='utf-8') as f:
#     f.write(','.join(col)+'\n')
#     for i in range(len(names)):
#         str='{},{},{}\n'.format(names[i],age[i],juso[i])
#         # print(str)
#         f.write(str)

# a=['one','two','three']
# # '연결문자'.join(리스트)
# print('-'.join(a))
# print('?'.join(a))
# print(type('?'.join(a)))
#
# b=('one','two','three')
# print('-'.join(b))
# print('?'.join(b))
# print(type('?'.join(b)))

# 이미지 저장
# import requests       #웹서버에 접근
# 이미지 저장(img src="https://'movie-phinf.pstatic.net/20201104_45/160445535053439akc_JPEG/movie_image.jpg')
# import requests
# url='https://movie-phinf.pstatic.net/20201104_45/160445535053439akc_JPEG/movie_image.jpg'
# recvd=requests.get(url)
# print(recvd)
# with open('img\\movie.jpg','wb') as f:          #b:binary
#     f.write(recvd.content)

