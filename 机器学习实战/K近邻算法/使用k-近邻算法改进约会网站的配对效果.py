import kNN
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
#datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')
#normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
#kNN.datingClassTest()
kNN.classifyPerson()
'''print(normMat)
print(datingDataMat)
print(datingDataMat.min(0))
print(datingLabels[0:20])'''
'''fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.xlabel('玩视频游戏所耗时间百分比')
plt.ylabel('每周消费的冰淇淋公升数')
plt.show()
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels), 15.0*array(datingLabels))
plt.xlabel('每年获得的飞行常客里程数')
plt.ylabel('玩视频游戏所耗时间百分比')
plt.show()'''