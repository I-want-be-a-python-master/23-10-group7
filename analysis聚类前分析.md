（目前完成了小提琴图、点图的绘制。热图还没有绘）



#### 小提琴图

首先讲述读取数据：

为了方便读取不同职业创建列表存储职业

```python
roles = ['mage', 'fighter', 'tank', 'assassin', 'support', 'marksman']
```

然后将每个职业的属性向量提取出来，文件中保存的数据类型是无符号数据，需要转换成int才能方便计算和操作

~~~python
# 读取数据
data = np.load('data/clean_lol_data.npy')
# 数据预处理
# 将每个职业的属性向量提取出来,注意进行数据类型转换--data = np.array(data, dtype=np.int32)
mage = np.array(data[data[:, 0] == roles[0], 1:5], dtype=np.int32)
fighter = np.array(data[data[:, 0] == roles[1], 1:5], dtype=np.int32)
tank = np.array(data[data[:, 0] == roles[2], 1:5], dtype=np.int32)
assassin = np.array(data[data[:, 0] == roles[3], 1:5], dtype=np.int32)
support = np.array(data[data[:, 0] == roles[4], 1:5], dtype=np.int32)
marksman = np.array(data[data[:, 0] == roles[5], 1:5], dtype=np.int32)
del data
~~~

小提琴图使用 plt.violinplot() 进行绘制

该函数中的小提琴可以当做对象拿出，并进行颜色的改变。



#### 点图

matplotlib 不提供绘制点图的方法。采取在同一张图中同时绘制误差线和折线的方法解决绘制点图的问题。

中心点及其误差线使用平均值和方差（或标准差）计算。

为了便于计算，需要将数据转成二维数组，数据长度不同，使用 np.nan 填充使其长度相同。

绘制攻击 点图示例代码如下

~~~python
data = [mage[:, 0], fighter[:, 0], tank[:, 0], assassin[:, 0], support[:, 0], marksman[:, 0]]
max_len = len(max(data, key=len))
data = [np.append(i, np.array([np.nan] * (max_len - len(i)))) for i in data]
data = np.column_stack(data)
# 计算平均值作为点
mean = np.nanmean(data, axis=0)
# 计算标准差作为误差线
std = np.nanstd(data, axis=0)/4 #除以4 是为了使图片更美观
plt.errorbar(roles, mean, yerr=std, ecolor='black', fmt='o', capsize=5, label='Data with Error Bars',linestyle='None')
plt.plot(mean) # 将点之间连接(可选)
plt.title('Pointplot')
plt.xlabel('Roles')
plt.ylabel('Attack')
plt.savefig('pic/pointplot_attack.png')
plt.show()
~~~



#### 热图

暂未解决