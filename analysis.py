import numpy as np
import matplotlib.pyplot as plt

data = np.load('clean_lol_data.npy')
roles = ['mage', 'fighter', 'tank', 'assassin', 'support', 'marksman']
colors = ['#1890FF', '#2FC25B', '#FACC14', '#223273', '#8543E0', '#13C2C2']
attributes = ['attack', 'defense', 'magic', 'difficulty']
# 绘制小提琴图
fig, axs = plt.subplots(2, 2, figsize=(10, 8), dpi=120)
for index, attribute in enumerate(attributes):
    ax = axs[index // 2, index % 2]
    data_attribute = []
    for role in roles:
        role_data_attribute = [int(item[attributes.index(attribute) + 1]) for item in data if item[0] == role]
        data_attribute.append(role_data_attribute)
    
    # 绘制小提琴图
    violin_parts = ax.violinplot(data_attribute, positions=np.arange(len(roles)), showmedians=True, showmeans=True)
    ax.set_xticks(np.arange(len(roles)))
    ax.set_xticklabels(roles, rotation=45, ha='right')
    
    # 设置小提琴图的细节
    for pc, color in zip(violin_parts['bodies'], colors):
        pc.set_facecolor(color)
    ax.set_title(f'Violin plot of {attribute} for each role')
    ax.set_xlabel('Role')
    ax.set_ylabel(attribute)

plt.tight_layout()
plt.savefig('violinplot.png')
plt.show()


# 绘制点图
fig, axs = plt.subplots(2, 2, figsize=(10, 8), dpi=120)
for index, attribute in enumerate(attributes):
    ax = axs[index // 2, index % 2]
    data_attribute = []
    for role in roles:
        role_data_attribute = [int(item[attributes.index(attribute) + 1]) for item in data if item[0] == role]
        data_attribute.append(role_data_attribute)
    max_len = len(max(data_attribute, key=len))
    data_attribute = [np.append(i, np.array([np.nan] * (max_len - len(i)))) for i in data_attribute]
    data_attribute = np.column_stack(data_attribute)
    
    # 计算平均值作为点
    mean = np.nanmean(data_attribute, axis=0)
    
    # 计算标准差作为误差线
    std = np.nanstd(data_attribute, axis=0)/4 #除以4 是为了使图片更美观
    ax.errorbar(roles, mean, yerr=std, ecolor='black', fmt='o', capsize=5, label='Data with Error Bars',linestyle='None')
    ax.plot(mean) # 将点之间连接(可选)
    ax.set_title(f'Point plot of {attribute} for each role')
    ax.set_xlabel('Role')
    ax.set_ylabel(attribute)

plt.tight_layout()
plt.savefig('pointplot.png')
plt.show()


# 绘制热图
data = np.array(data[:, 1:], dtype=np.int32)
# 计算相关系数
data_corr = np.corrcoef(data.T)
# 根据相关系数矩阵绘图
plt.imshow(data_corr, cmap='viridis',vmax=1, vmin=-1)
plt.colorbar()
plt.xticks([0, 1, 2, 3], ['attack', 'defense', 'magic', 'difficulty'])
plt.yticks([0, 1, 2, 3], ['difficulty', 'magic', 'defense', 'attack'])
plt.title('heatmap')
plt.savefig('heatmap.png')
plt.show()
