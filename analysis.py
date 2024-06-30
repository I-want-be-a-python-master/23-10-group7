import numpy as np
import matplotlib.pyplot as plt

# 一个存储职业的列表
roles = ['mage', 'fighter', 'tank', 'assassin', 'support', 'marksman']

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
# 小提琴图有四张:分别关于攻击\防御\魔力\上手难度
# 攻击
# 设置颜色
colors = ['#1890FF', '#2FC25B', '#FACC14', '#223273', '#8543E0', '#13C2C2', '#3436c7', '#F04864']
vp = plt.violinplot([mage[:, 0], fighter[:, 0], tank[:, 0], assassin[:, 0], support[:, 0], marksman[:, 0]],
               showmeans=True, showmedians=True)
for i, body in enumerate(vp['bodies']):
    body.set_facecolor(colors[i])
plt.title('Violinplot')
plt.xlabel('Roles')
plt.ylabel('Attack')
plt.xticks(np.arange(1, 7), roles)
plt.savefig('pic/violinplot_attack.png')
plt.show()

# 防御
vp = plt.violinplot([mage[:, 1], fighter[:, 1], tank[:, 1], assassin[:, 1], support[:, 1], marksman[:, 1]],
               showmeans=True, showmedians=True)
for i, body in enumerate(vp['bodies']):
    body.set_facecolor(colors[i])
plt.title('Violinplot')
plt.xlabel('Roles')
plt.ylabel('Defense')
plt.xticks(np.arange(1, 7), roles)
plt.savefig('pic/violinplot_defense.png')
plt.show()

# 魔力
vp = plt.violinplot([mage[:, 2], fighter[:, 2], tank[:, 2], assassin[:, 2], support[:, 2], marksman[:, 2]],
               showmeans=True, showmedians=True)
for i, body in enumerate(vp['bodies']):
    body.set_facecolor(colors[i])
plt.title('Violinplot')
plt.xlabel('Roles')
plt.ylabel('Magic')
plt.xticks(np.arange(1, 7), roles)
plt.savefig('pic/violinplot_magic.png')
plt.show()

# 上手难度
vp = plt.violinplot([mage[:, 3], fighter[:, 3], tank[:, 3], assassin[:, 3], support[:, 3], marksman[:, 3]],
               showmeans=True, showmedians=True)
for i, body in enumerate(vp['bodies']):
    body.set_facecolor(colors[i])
plt.title('Violinplot')
plt.xlabel('Roles')
plt.ylabel('Difficulty')
plt.xticks(np.arange(1, 7), roles)
plt.savefig('pic/violinplot_difficulty.png')
plt.show()




# 绘制点图
# 攻击
# 处理数据为二维数组,使用np.nan填充使一维数组长度相同
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


# 防御
data = [mage[:, 1], fighter[:, 1], tank[:, 1], assassin[:, 1], support[:, 1], marksman[:, 1]]
max_len = len(max(data, key=len))
data = [np.append(i, np.array([np.nan] * (max_len - len(i)))) for i in data]
data = np.column_stack(data)
mean = np.nanmean(data, axis=0)
std = np.nanstd(data, axis=0)/4
plt.errorbar(roles, mean, yerr=std, ecolor='black', fmt='o', capsize=5, label='Data with Error Bars',linestyle='None')
plt.plot(mean) # 将点之间连接(可选)
plt.title('Pointplot')
plt.xlabel('Roles')
plt.ylabel('Defense')
plt.savefig('pic/pointplot_defense.png')
plt.show()

# 魔力
data = [mage[:, 2], fighter[:, 2], tank[:, 2], assassin[:, 2], support[:, 2], marksman[:, 2]]
max_len = len(max(data, key=len))
data = [np.append(i, np.array([np.nan] * (max_len - len(i)))) for i in data]
data = np.column_stack(data)
mean = np.nanmean(data, axis=0)
std = np.nanstd(data, axis=0)/4
plt.errorbar(roles, mean, yerr=std, ecolor='black', fmt='o', capsize=5, label='Data with Error Bars',linestyle='None')
plt.plot(mean) # 将点之间连接(可选)
plt.title('Pointplot')
plt.xlabel('Roles')
plt.ylabel('Magic')
plt.savefig('pic/pointplot_magic.png')
plt.show()

# 上手难度
data = [mage[:, 3], fighter[:, 3], tank[:, 3], assassin[:, 3], support[:, 3], marksman[:, 3]]
max_len = len(max(data, key=len))
data = [np.append(i, np.array([np.nan] * (max_len - len(i)))) for i in data]
data = np.column_stack(data)
mean = np.nanmean(data, axis=0)
std = np.nanstd(data, axis=0)/4
plt.errorbar(roles, mean, yerr=std, ecolor='black', fmt='o', capsize=5, label='Data with Error Bars',linestyle='None')
plt.plot(mean) # 将点之间连接(可选)
plt.title('Pointplot')
plt.xlabel('Roles')
plt.ylabel('Difficulty')
plt.savefig('pic/pointplot_difficulty.png')
plt.show()


# 绘制热图
# 重新读取数据
data = np.load('data/clean_lol_data.npy')
data = np.array(data[:, 1:], dtype=np.int32)
# 计算相关系数
data_corr = np.corrcoef(data.T)
# 根据相关系数矩阵绘图
plt.imshow(data_corr, cmap='viridis',vmax=1, vmin=-1)
plt.colorbar()
plt.xticks([0, 1, 2, 3], ['attack', 'defense', 'magic', 'difficulty'])
plt.yticks([0, 1, 2, 3], ['difficulty', 'magic', 'defense', 'attack'])
plt.title('heatmap')
plt.savefig('pic/heatmap.png')
plt.show()