# import calc  #자기가 만든 파일도 import 가능 #print문 안에 있으면 자동으로 뜸
# print(calc.add(3,4))
# print(calc.sub(3,4))
# print(calc.mul(3,4))
# print(calc.div(3,4))

# from calc import add,sub #calc중에 add랑 sub만 import
# print(add(10,100))
# print(sub(5,1))
# print(mul(5,1)) #사용불가

from calc import add as a,sub as s #calc중에 add는 a sub는 s로 import

print(a(10,100))
print(s(5,1))
