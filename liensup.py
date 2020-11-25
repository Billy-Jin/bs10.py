# import numpy as np

# x=np.array([1,2,3])
# # print(x)
# # print(type(x))
# x[0]=10
# y=np.array([4,5,6])
# print(x+y)

# print(np.arange(10))
# print(np.arange(5,10))

# x=np.array([[1,2,3],[4,5,6]])
# print(x)
# print(x.shape)
# w,h = x.shape
# print(w)
# print(h)
# print(x[1,2])
#
# print(np.zeros((3,10)))
# print(np.random.rand(2,3))

# a=np.arange(10)
# print(a)

# print(a.reshape(2,5))
#
# x=np.array([[4,4,4],[8,8,8]])
# y=np.array([[1,1,1],[2,2,2]])
# z=np.array([[3,3,3],[4,4,4]]) #행렬이 모두 동일해야 계산 가능
# print(x+y)
# print(x+z)

# v=np.array([[1,2,3],[4,5,6]])
# w=np.array([[1,1],[2,2],[3,3]])
# z=np.array([[1,2,3],[4,5,6]])
# # print(v.dot(w))
# print(v*z)

# x=np.array([1,1,2,3,5,8,13])
# # print(x>3)
# print(x[x>3])

# 리스트 1-(1)
import numpy as np

from matplotlib import pyplot as plt


#data 작성
# np.random.seed(1)
# x=np.arange(10)
# y=np.random.rand(10)
x=[0,1,2,3,4]
y=[0,1,4,9,16]


plt.plot(x,y)
plt.show()