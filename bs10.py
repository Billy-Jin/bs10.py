# import requests
# import re
# url='https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
# recvd=requests.get(url)
# # print(recvd)
# locations=re.findall(r'<location wl_ver="3">(.+?)</location>',recvd.text,re.DOTALL)
# # print(len(locations))
# for location in locations:
#     # print(location)
#     # province=re.findall(r'<province>.+?</province>',location,re.DOTALL)
#     # city=re.findall(r'<city>.+?</city>',location,re.DOTALL)
#     # print(province,city)
#     pc=re.findall(r'<province>(.+?)</province>.+?<city>(.+?)</city>',location,re.DOTALL)
#     # print(pc) #pc[0]=('서울ㆍ인천ㆍ경기도', '서울')
#     province=pc[0][0] #서울ㆍ인천ㆍ경기도
#     city=pc[0][1]   #서울
#     # print(province)
#     # print(city)
#     datas=re.findall(r'<data>(.+?)</data>',location,re.DOTALL)
#     # print(len(data))
#     for data in datas:
#         # print(data)
#         temps=re.findall(
#             r'<mode>(.+?)</mode>.+?<tmEf>(.+?)</tmEf>.+?<wf>(.+?)</wf>.+?<tmn>(.+?)</tmn>.+?<tmx>(.+?)</tmx>.+?<reliability>(.*?)</reliability>.+?<rnSt>(.+?)</rnSt>'
#             ,data,re.DOTALL)
#         # print(temps)
#         mode=temps[0][0]
#         tmEf=temps[0][1]
#         wf=temps[0][2]
#         tmn=temps[0][3]
#         tmx=temps[0][4]
#         reliability=temps[0][5]
#         rnSt=temps[0][6]
#         str='{},{},{},{},{},{},{},{},{}'
#         print(str.format(province,city,mode,tmEf,wf,tmn,tmx,reliability,rnSt))


#-------------------------------------
import re
print(re.search('ca{2}t','ct'))
print(re.search('ca{2}t','caat'))
print(re.search('ca{2,}t','caaat'))
print(re.search('ca{2,5}t','caaaaat'))
print(re.search('ca?t','ct'))
print(re.search('ca?t','cat'))
print(re.search('ca?t','caat'))

# sub(바꿀문자열,대상문자열)      치환
color=re.compile('(blue|green|red)')
print(color.sub('pink','orange book and green dress and red socks'))
