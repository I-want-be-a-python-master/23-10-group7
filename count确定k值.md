# K-Means聚类分析

本文档描述了如何使用Python和`sklearn`库，通过肘部法则和轮廓系数法来确定最佳的k-mean聚类数（k值）。

## 肘部法则 (Elbow Method)

肘部法则是一种启发式方法，用于确定K-Means聚类中的最佳聚类数。该方法基于聚类内的方差（SSE，平方误差和）来评估不同聚类数的效果。随着聚类数的增加，SSE会逐渐减小，但在某个点之后，SSE的减小幅度会显著减小，这个点通常被认为是最佳的聚类数。

**公式：**
$$
\text{SSE} = \sum_{i=1}^{n} \| x_i - \mu_k \|^2
$$
其中，x_i是属于第 𝑘 个聚类的点，μ_k 是该聚类的中心点，n 是聚类内的点的数量。

## 轮廓系数法 (Silhouette Score)

轮廓系数是一种衡量样本聚类质量的指标，其值的范围是[-1, 1]。轮廓系数较高的聚类被认为是好的聚类。轮廓系数考虑了聚类内部的凝聚度和聚类之间的分离度。

**公式：**
$$
\text{Silhouette}(o_i) = \frac{b_i - a_i}{\max(a_i, b_i)}
$$
其中，

- \( a_i \) 是第 \( i \) 个样本与其同一聚类中所有其他样本的平均距离。
- \( b_i \) 是第 \( i \) 个样本与最近聚类中所有样本的平均距离。

## 实现步骤

1. **数据加载与预处理**：
   加载数据，并将其转换为数值类型以供聚类分析使用。

2. **计算SSE**：
   使用`calculate_sse`函数计算不同K值下的SSE。

3. **绘制肘部图**：
   绘制SSE随K值变化的图，以确定最佳聚类数。

4. **计算轮廓系数**：
   使用`calculate_silhouette`函数计算不同K值下的轮廓系数。

5. **绘制轮廓系数图**：
   绘制轮廓系数随K值变化的图，以辅助确定最佳聚类数。

6. **选择最佳聚类数**：
   根据轮廓系数选择最大的K值作为最佳聚类数。

## 代码实现

以下是使用Python和`sklearn`库进行K-Means聚类分析的示例代码。

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# 假设 data 是你的 NumPy 数组
data = np.load('clean_lol_data.npy')
data_numeric = data[:, 1:].astype(int)

# 定义计算SSE的函数
def calculate_sse(data, k):
    kmeans = KMeans(n_clusters=k, random_state=0).fit(data)
    return kmeans.inertia_

# 定义计算轮廓系数的函数
def calculate_silhouette(k, data):
    kmeans = KMeans(n_clusters=k, random_state=42).fit(data)
    score = silhouette_score(data, kmeans.labels_)
    return score

# 尝试不同的 K 值并计算 SSE 和轮廓系数
k_values = range(1, 11)
sse_list = [calculate_sse(data_numeric, k) for k in k_values]
silhouette_scores = [calculate_silhouette(k, data_numeric) for k in range(2, 11)]

# 绘制肘部图和轮廓系数图
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.plot(k_values, sse_list, '-o')
plt.xlabel('Number of clusters K')
plt.ylabel('SSE (Sum of Squared Errors)')
plt.title('Elbow Method For Optimal K')

plt.subplot(1, 2, 2)
plt.plot(k_values[1:], silhouette_scores, '-o')
plt.xlabel('Number of clusters K')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Scores For Different K Values')
plt.show()

# 选择轮廓系数最大的 K 值
best_k = k_values[1:][np.argmax(silhouette_scores)]
print(f"Best K value based on silhouette score: {best_k}")
```


