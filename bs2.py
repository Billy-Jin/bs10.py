from bs4 import BeautifulSoup

with open('data\\test.html',mode='r',encoding='utf-8') as f:
    txt=f.read()
    # print(txt)
    # print(type(txt))
    # print('-'*40)
    dom=BeautifulSoup(txt,'lxml')
    # div=dom.find('div')
    # print(div)
    # divs=dom.find_all('div')
    # print(divs)
    # div태그중에 클래스가 'ex_class' 인것중 첫번째 추출
    # divs=dom.find('div',{'class':'ex_class'})
    # print(divs)
    # div태그중에 클래스가 'ex_class' 인것 모두 추출
    # divs=dom.find_all('div',{'class':'ex_class'})
    # print(divs)
    # 클래스가 'ex_class' 인것 모두 추출
    # divs=dom.find_all(class_='ex_class')
    # print(divs)
    # id가 'ex_id' 인것 추출 //id는 공통된 이름 불가능 하므로 하나가 최대이다.여러개 불가
    # ids=dom.find(id='ex_id')
    # print(ids)

    # id가 'ex_id'인것 중에 모든 p태그 추출
    # ps=ids.find_all('p')
    # print(ps)

    #data 추출-------------------
    #   dom.string
    #   dom.text
    #   dom.get_text()
    # 속성추출--------------------
    # dom['속성']
    # dom.get('속성')
    # dom.attrs['속성']


    # title=dom.find('title')
    # print(title)
    # print(title.string)
    # print(title.text)
    # print(title.get_text())
    # # a의 내용추출
    # aes = dom.find_all("a")
    # # print(aes)  #list
    # for a in aes:
    #     print(a.text)
    #     print(a['href']) #
    #id가 link2인 요소의 class 추출
    # print(dom.find(id='link2').get('class'))
    #DOM추적
    # dom.parent 부모
    # dom.parents 조상, 객체로 반환
    # dom.children 자식
    # dom.descendants 자손


    title=dom.find('p',class_='title')
    # print(title)
    # print('-'*30)
    # print('parent',title.parent)
    # print('-' * 30)
    # print('parents',title.parents)
    # for p in title.parents:
    #     print(p)
    #     print('-'*30)
    #id가 second인 div
    div=dom.find(id='second')
    # print(div)
    # divchild=div.children
    # print('-'*30)
    # print(divchild)
    # for c in divchild:
    #     print(c)
    #     print('!'*30)
    divdes=div.descendants
    print(divdes)
    print('-'*30)
    for d in divdes:
        print(d)
        print('!'*30)
    # id가 link2인 a의 형제찾기
    a=dom.find(id='link2')
    print(a)
    anext=a.next_sibling
    print(anext)
    for temp in anext:
        print(temp)
        print('$'*30)







# os.path.join()