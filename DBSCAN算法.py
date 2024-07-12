
import random
import numpy as np
import matplotlib.pyplot as plt
class DBSCAN(object):
    def __init__(self,eps,MinPts):
        """
        :param eps:领域半径
        :param MinPts:成为核心对象的在领域半径内的最少点数
        """
        self.eps = eps
        self.MinPts = MinPts
    def fit(self,X):
        # 初始化数据点状态及索引号
        self.X = np.array(X)
        global index,state,class_cluster
        index = [i for i in np.arange(X.shape[0])]
        state = [0] * X.shape[0]
        class_cluster = 1
        while 1:#计算部分
            if self.choice() is not None:
                # 从未划分的数据点中随机选择一个
                point = self.choice()
                # 计算在其领域半径内的点
                not_use_index = self.not_use_point()
                temp = []
                for i in not_use_index:
                    if i != point:
                        if self.cal_dist(self.X[i, :], self.X[point, :]) <= self.eps:
                            temp.append(i)
                if len(temp) >= self.MinPts:
                    self.cal_eps_count([point])
                    class_cluster += 1
                else:
                    state[point] = "noise"
            else:
                break
    return state
    def cal_eps_count(self,points):
        flag = []
        for point in points:
            temp = []
            for i in self.not_use_point():
                if self.cal_dist(self.X[i,:],self.X[point,:]) <= self.eps and i != point:
                    state[i] = class_cluster
                    temp.append(i)
            if len(temp) >= self.MinPts:
                flag += temp
        if flag:
            return self.cal_eps_count(flag)
    def cal_dist(self,x1,x2):
        return (((x1-x2)**2).sum())**0.5
    def not_use_point(self):
        temp = []
        for i in index:
            if state[i] in [0,"noise"]:
                temp.append(i)
        return temp
    def choice(self):
        temp = []
        for i in index:
            if state[i] == 0:
                temp.append(i)
        if len(temp) == 1:
            state[temp[0]] = "noise"
            return None
        elif len(temp) == 0:
            return None
        else:
            return random.choice(temp)
if __name__ == '__main__':
    dbscan = DBSCAN(eps=4,MinPts=2)
    # 提取特征
    data = np.load('data\clean_lol_data.npy')
    X = data[:, 1:5]
    X = X.astype(int)
    y = dbscan.fit(X)
    print(y)
    plt.figure()
    plt.subplot(4, 4, 2)
    plt.scatter(X[:,0],X[:,1],c=[["r", "b"][i-1] if i != "noise" else "g" for i in y])
    plt.subplot(4, 4, 3)
    plt.scatter(X[:, 0], X[:,2], c=[["r", "b"][i - 1] if i != "noise" else "g" for i in y])
    plt.subplot(4, 4, 4)
    plt.scatter(X[:, 0], X[:,3], c=[["r", "b"][i - 1] if i != "noise" else "g" for i in y])
    plt.subplot(4, 4, 5)
    plt.scatter(X[:,1], X[:,0], c=[["r", "b"][i - 1] if i != "noise" else "g" for i in y])
    plt.subplot(4, 4, 7)
    plt.scatter(X[:, 1], X[:,2], c=[["r", "b"][i - 1] if i != "noise" else "g" for i in y])
    plt.subplot(4, 4, 8)
    plt.scatter(X[:, 1], X[:,3], c=[["r", "b"][i - 1] if i != "noise" else "g" for i in y])
    plt.subplot(4, 4, 9)
    plt.scatter(X[:,2], X[:,0], c=[["r", "b"][i - 1] if i != "noise" else "g" for i in y])
    plt.subplot(4, 4, 10)
    plt.scatter(X[:,2], X[:,1], c=[["r", "b"][i - 1] if i != "noise" else "g" for i in y])
    plt.subplot(4, 4, 12)
    plt.scatter(X[:,2], X[:,3], c=[["r", "b"][i - 1] if i != "noise" else "g" for i in y])
    plt.subplot(4, 4, 13)
    plt.scatter(X[:,3], X[:, 0], c=[["r", "b"][i - 1] if i != "noise" else "g" for i in y])
    plt.subplot(4, 4, 14)
    plt.scatter(X[:, 3], X[:, 1], c=[["r", "b"][i - 1] if i != "noise" else "g" for i in y])
    plt.subplot(4, 4, 15)
    plt.scatter(X[:,3], X[:,2], c=[["r", "b"][i - 1] if i != "noise" else "g" for i in y])
    
    plt.show()
