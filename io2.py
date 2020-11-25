# def f1(n):
#     return n*10
#
# print(f1(5))
# a=f1
# print(type(a))
# print(a(10))

#람다함수:메모리 절약, 가독성 향상, 코드 간결
# lambda 매개변수:반환값

# b=lambda n:n*10
# print(b(10))
# print('-'*10)
# def f2(x,y,f):
#     print(x*y*f(x+y))
#
# f2(10,100, lambda n:n+1) #n자리에 (x+y)된 값이 들어감 x+y=n //매개변수 여러개면 ,로 구분
#-----------------------------------------------------

# a=[1,2,3,4,5] #--> [3,6,9,12,15]
# b=lambda x:x*3
# print(b(a))
# def f3(x):
#     result=[]
#     for i in x:
#         result.append(i*3)
#     return result
# print(f3(a))

#map(함수명,반복가능객체):매개변수로 함수와 반복가능 객체를 입력
# def f4(x):
#     return x*3
# print(f4(7))
# print(f4([1,2,3]))
# print(map(f4,[1,2,3]))
# print(list(map(f4,[1,2,3])))
# print(list(map(lambda n:n/4,[4,8,12])))
# print(list(map(int,list(map(lambda n:n/4,[4,8,12])))))

#---------------------------
import os
import glob
# 파일경로 리눅스, 맥에서는 / 윈도우에서는 \사용
# os모듈: 디렉토리, 파일등의 os자원 제어
# glob모듈
# print('현재 작업디렉토리',os.getcwd()) #current working directory
# print('현재 작업디렉토리의 목록',os.listdir())
# print('d:\목록',os.listdir('d:\\'))
# print(os.listdir('D:\\down\\erd'))
# print(os.path.join('..','test1')) #경로생성
# print(os.listdir(os.path.join('..','test1')))
# print(os.path.join('..','test1','Scripts'))
# print(os.listdir(os.path.join('..','test1','Scripts')))
# with open('data\\webtoon.csv','w',encoding='utf*8') as f:
#     pass
# with open(os.path.join('data\\webtoon.csv'),'w',encoding='utf*8') as f:
#     pass#나중에 생각 하겠다

# print(glob.glob('*')) #현재위치 모든파일 반환
# print(glob.glob('*.py')) #현재위치 확장자가 py인것 파일 반환
# f1='D:\\oraclestudy\\pj1\\data\\Beauti.smi'
# print(os.path.dirname(f1))
# print(os.path.basename(f1)) #가장 마지막에 있는 이름(파일이든 디렉토리든 무엇이든지)
#---------------------------
# f=open(os.path.join('data','Beauty.smi'))
# # print(f.read()) # 전체 다 읽음
# # print(f.readline()) #한줄 읽고 끝
# print(f.readlines()) #리스트로 반환
# f.close()
# f=open(os.path.join('data','Beauty.smi'))
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line,end='') #줄 바꿈 하지 마라
# f.close()
#----data폴더의 모든 파일 내용 출력--------------------------
# filelist=glob.glob(os.path.join('data','*'))
# print(filelist)
# for file in filelist:
#     with open(file,encoding='utf-8') as f:
#         print(f.read())
#         print("-"*30)
# 'Beauty.smi' --> [자막만] --> 'Beauty.txt'----------------------------------
# inputFile='data\\beauty.smi'
def makeTxt(inputFile):
    f=open(inputFile,encoding='utf-8')
    result=[]
    for line in f:
        line=line.replace('\n','')
        if len(line)<4:
            continue
        elif line.count(':')>3:
            continue
        line=line.replace('<b>','')
        line=line.replace('</b>','')
        line=line.replace('<i>','')
        line=line.replace('</i>','')
        # print(line)
        result.append(line)
        # print(line.count(':'))
    f.close()
    return result

def makeFile(inputFile,temp):
    filename=inputFile[:-3]+'txt'
    print(filename)
    with open(filename,'w',encoding='utf-8') as fw:
        for t in temp:
            fw.write(t+'\n')
def main():
    inputFile='data\\beauty.smi'
    temp=makeTxt(inputFile)
    # print(temp)
    makeFile(inputFile,temp)

if __name__=='__main__':
    main()

# import cchardet  #인토딩 확이 ㄴ하고 인코딩별 파일 읽어오는 소스스
# or dir in glob.glob(os.path.join('data', '*')):
#     encoding = None;
#
#     with open(dir, 'rb') as f:
#         encoding = cchardet.detect(f.read())['encoding']
#         with open (dir, 'r', encoding=encoding) as ff:
#             print(ff.readlines())