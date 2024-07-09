import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# 加载预处理后的数据
data = np.load('data/clean_lol_data.npy')

# 首先将字符串转换为数值类型
data_numeric = data[:, 1:].astype(int)  # 只转换数值列，舍弃第一列（英雄职业）

# 定义一个函数来计算不同 K 值的 SSE（平方误差和）
def calculate_sse(data, k):
    kmeans = KMeans(n_clusters=k, random_state=0).fit(data)
    return kmeans.inertia_

# 定义一个函数来计算不同 K 值的轮廓系数
def calculate_silhouette(k, data):
    kmeans = KMeans(n_clusters=k, random_state=42).fit(data)
    score = silhouette_score(data, kmeans.labels_)
    return score

# 尝试不同的 K 值并计算 SSE
k_values = range(1, 11)
sse_list = [calculate_sse(data_numeric, k) for k in k_values]

# 绘制肘部图
plt.figure(figsize=(8, 6))
plt.plot(k_values, sse_list, '-o')
plt.xlabel('Number of clusters K')
plt.ylabel('SSE (Sum of Squared Errors)')
plt.title('Elbow Method For Optimal K')
plt.savefig('pic/elbow_method.png')
plt.show()

# 尝试不同的 K 值并计算轮廓系数
k_values = range(2, 11)  # 轮廓系数对单簇没有意义
silhouette_scores = [calculate_silhouette(k, data_numeric) for k in k_values]

# 绘制轮廓系数图
plt.figure(figsize=(8, 6))
plt.plot(k_values, silhouette_scores, '-o')
plt.xlabel('Number of clusters K')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Scores For Different K Values')
plt.savefig('pic/silhouette_scores.png')
plt.show()

# 选择轮廓系数最大的 K 值
best_k = k_values[np.argmax(silhouette_scores)]
print(f"Best K value based on silhouette score: {best_k}")