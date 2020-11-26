# import requests
# from bs4 import BeautifulSoup
#
# def saveImg(imgUrl,title):
#     # print(imgUrl)
#     # print(imgUrl.index('?'))
#     # print(imgUrl[imgUrl.index('?')-4:imgUrl.index('?')])
#     # print(title)
#     title=title.replace('[','')
#     title=title.replace(']','')
#     title=title.replace("'",'')
#     title=title.replace(".",'')
#     title=title.replace(",",'')
#     title=title.replace("?",'')
#     filename='img\\'+title+imgUrl[imgUrl.index('?')-4:imgUrl.index('?')]
#     print(filename)
#     r=requests.get(imgUrl)
#     f=open(filename,'wb')
#     f.write(r.content)
#     f.close()
# def makeData(pageUrl):
#     r=requests.get(pageUrl)
#     # print(r)
#     d=BeautifulSoup(r.text,'lxml')
#     imgUrl=d.find('div',id="newsEndContents").find('img')['src']
#     title=d.find('h4').text
#     # print(imgUrl)
#     # print(title)
#     content=d.find('div',id='newsEndContents').text
#     # print(content)
#     str='{}::\n{}'.format(title,content)
#     # print(str)
#     saveImg(imgUrl,title)
#
# url='https://sports.news.naver.com/index.nhn'
# recvd=requests.get(url)
# # print(recvd)
# # print(recvd.text)
# dom=BeautifulSoup(recvd.text,'lxml')
# aes=dom.find_all('a',class_='link_today')
# # print(len(aes))
# for a in aes:
#     # print(a['href'])
#     pageUrl='https://sports.news.naver.com'+a['href']
#     # print(pageUrl)
#     makeData(pageUrl)


#----------------------------------------------
import requests
import re
from bs4 import BeautifulSoup

# def saveImg(imgUrl,title):
#     # print(imgUrl)
#     # print(imgUrl[-4:])
#     # print(title)
#     title=title.replace('[','')
#     title=title.replace(']','')
#     title=title.replace('|','')
#     title=title.replace("'",'')
#     title=title.replace(".",'')
#     title=title.replace(",",'')
#     title=title.replace("?",'')
#     title=title.replace("\n",'')
#     filename='img\\'+title+imgUrl[-4:]
#     print(filename)
#     r=requests.get(imgUrl)
#     f=open(filename,'wb')
#     f.write(r.content)
#     f.close()

def makeData(pageUrl):
    r=requests.get(pageUrl)
    # print(r)
    d=BeautifulSoup(r.text,'lxml')
    # dd=d.find('div',class_='centeredcrop')
    # # dd=d.find('img',id='main_thumbs')
    # print(dd)
    imgUrl=d.find('div',class_="centeredcrop").find('img')['src']
    title=d.find('h3').text
    # print(imgUrl)
    # print(title)

    #재료
    a=d.find('div',class_="cont_ingre2")
    ul=a.find_all('ul')
    # print(ul)
    k = 1
    for i in ul:
        li=i.find_all('li')
        # print(li)
        material=[]
        source=[]
        for j in li:
            j=j.text.replace(' ', '')
            j=j.replace('\n',' ')
            # print(j)
            #print(j.text.replace(' ',''))
            if k==1:
                material.append(j)
                # print('재료:',j)
            elif k==2:
                source.append(j)
                # print('양념:',j)
        k+=1

    #조리순서
    sunse = d.find('div', class_='view_step')
    st=re.compile(r'stepDiv.+?')
    sun=sunse.find_all('div',id=st)
    # print(sunse)
    # print(sun)
    # print(len(sun))
    j=1
    for i in sun:
        step=i.find('div',id='stepdescr{}'.format(j)).text
        img=i.find('img')['src']
        # print(str(j)+')'+step)
        # print(img)
        j+=1
        # with open('data\\recipe.txt','a',encoding='utf-8') as f:


    # content=d.find('div',id='stepdescr1').text
    # print(content)
    # str='{}::\n{}'.format(title,content)
    # print(str)
    # saveImg(imgUrl,title)

url='https://www.10000recipe.com/recipe/list.html?q=%EB%B0%91%EB%B0%98%EC%B0%AC'
recvd=requests.get(url)
# print(recvd)
# print(recvd.text)
dom=BeautifulSoup(recvd.text,'lxml')
aes=dom.find_all('a',class_="common_sp_link")
# print(len(aes))


for a in aes:
    # print(a['href'])
    pageUrl='https://www.10000recipe.com'+a['href']
    # print(pageUrl)
    makeData(pageUrl)
    break
# div=dom.find_all('div',class_='common_sp_caption_tit line2')
# print(div)