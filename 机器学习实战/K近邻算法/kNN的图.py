from numpy import *
import operator
import matplotlib.pyplot as plt

def createDataSet():
    a = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return a, labels

a, labels = createDataSet()

# 提取每个数据点的x和y坐标
x = a[:, 0]
y = a[:, 1]

# 绘制散点图
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter plot of data points')
plt.show()

