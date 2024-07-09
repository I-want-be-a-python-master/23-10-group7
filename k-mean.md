# K-Means聚类可视化

本文档描述了如何使用Python、`matplotlib`库和`sklearn`库进行K-Means聚类分析，并在二维空间中可视化聚类结果。

## K-Means聚类简介

K-Means聚类是一种无监督学习算法，用于将数据点划分为K个簇。每个簇由其质心（即簇内所有点的中心点）定义。算法的目标是最小化簇内误差，即簇内所有点到质心的距离之和。

### 算法步骤：
1. 随机选择K个数据点作为初始质心。
2. 将每个数据点分配到最近的质心，形成K个簇。
3. 重新计算每个簇的质心，作为簇内所有点的均值。
4. 重复步骤2和3，直到质心不再显著变化或达到预定迭代次数。

## 实现步骤

1. **数据加载与预处理**：
   加载数据，并将其转换为数值类型以供聚类分析使用。

2. **实例化KMeans对象**：
   使用`sklearn.cluster`中的`KMeans`类创建K-Means聚类模型。

3. **模型拟合**：
   使用数据拟合K-Means模型。

4. **聚类标签预测**：
   预测每个数据点的聚类标签。

5. **降维**：
   使用PCA（主成分分析）进行降维至二维，以便于可视化。

6. **可视化聚类结果**：
   绘制聚类结果，包括簇内数据点和簇中心。

## 代码实现

以下是使用Python和`sklearn`库进行K-Means聚类分析并可视化聚类结果的示例代码。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# 加载数据
data = np.load('clean_lol_data.npy')
numeric_data = data[:, 1:].astype(int)

# 实例化 KMeans 对象
kmeans = KMeans(n_clusters=4, random_state=0)

# 拟合模型
kmeans.fit(numeric_data)

# 预测每个数据点的聚类标签
predicted_labels = kmeans.predict(numeric_data)

# 使用 PCA 进行降维
pca = PCA(n_components=2)
numeric_data_reduced = pca.fit_transform(numeric_data)

# 可视化聚类结果
plt.figure(figsize=(8, 6))
colors = ['r', 'g', 'b', 'y']  # 为每个簇定义颜色
for i in range(4):
    cluster_data = numeric_data_reduced[predicted_labels == i]
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1], c=colors[i], label=f'Cluster {i+1}')

# 绘制簇中心
centers_reduced = pca.transform(kmeans.cluster_centers_)
plt.scatter(centers_reduced[:, 0], centers_reduced[:, 1], s=300, c='k', label='Centroids')

plt.title('K-means Clustering')
plt.legend()
plt.show()
```
