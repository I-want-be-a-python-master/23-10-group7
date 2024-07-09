"""
k=4 由 count.py 文件得出
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA  # 用于降维

# 加载数据
data = np.load('data/clean_lol_data.npy')

# 分离数值数据
numeric_data = data[:, 1:].astype(int)

# 实例化 KMeans 对象
kmeans = KMeans(n_clusters=4, random_state=0)

# 拟合模型
kmeans.fit(numeric_data)

# 预测每个数据点的聚类标签
predicted_labels = kmeans.predict(numeric_data)

# 如果数据是多维的，使用 PCA 进行降维
pca = PCA(n_components=2)  # 降维到2维
numeric_data_reduced = pca.fit_transform(numeric_data)

# 可视化聚类结果
plt.figure(figsize=(8, 6))
colors = ['r', 'g', 'b', 'y']  # 为每个簇定义颜色
for i in range(4):
    # 选择当前簇的数据点
    cluster_data = numeric_data_reduced[predicted_labels == i]
    # 绘制当前簇的数据点
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1], c=colors[i], label=f'Cluster {i+1}')

# 绘制簇中心
centers_reduced = pca.transform(kmeans.cluster_centers_)
plt.scatter(centers_reduced[:, 0], centers_reduced[:, 1], s=300, c='k', label='Centroids')

plt.title('K-means Cluster')
plt.legend()
plt.savefig('pic/k-means_cluster.png')
plt.show()