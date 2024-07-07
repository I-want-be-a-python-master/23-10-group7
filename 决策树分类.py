import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree

data = np.load('clean_lol_data.npy')
columns = ['roles', 'attack', 'defense', 'magic', 'difficulty']

# 对数据进行可视化
plt.figure(figsize=(15, 15), dpi=60)
for i in range(4):
    for j in range(4):
        plt.subplot(4, 4, i * 4 + j + 1)
        if i == 0:
            plt.title(columns[j + 1])
        if j == 0:
            plt.ylabel(columns[i + 1])
        if i == j:
            plt.text(0.3, 0.4, columns[i + 1], fontsize=15)
            continue
        # 对数据类型进行转化
        if i == 0:
            plt.scatter(np.array([int(item[j]) for item in data]), data[:, i],
                        c=np.array([int(item[-1]) for item in data]), cmap='brg')
        elif j == 0:
            plt.scatter(data[:, j], np.array([int(item[i]) for item in data]),
                        c=np.array([int(item[-1]) for item in data]), cmap='brg')
        else:
            plt.scatter(np.array([int(item[j]) for item in data]), np.array([int(item[i]) for item in data]),
                        c=np.array([int(item[-1]) for item in data]), cmap='brg')

plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.suptitle('roles\nfighter | mage | tank | assassin | support | marksman', fontsize=20)
plt.savefig('scatter.png')
plt.show()

# 对数据进行切分，分出训练集和测试集
all_inputs = data[:, 1:]
all_classes = data[:, 0]
X_train, X_test, Y_train, Y_test = train_test_split(all_inputs,
                                                    all_classes, train_size=0.8, random_state=1)

# 使用决策树算法进行训练
# 定义决策树对象
dtc = tree.DecisionTreeClassifier(criterion='entropy', min_samples_leaf=8)
# 训练模型
model = dtc.fit(X_train, Y_train)
# 输出所得模型的准确性
print('测试集准确性：', dtc.score(X_test, Y_test))  # 测试集
print('训练集准确性：', dtc.score(X_train, Y_train))  # 训练集
print('总准确性：', dtc.score(all_inputs, all_classes))

# 决策树的可视化
font2 = {'weight': 'normal',
         'size': 20, }
mpl.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(20, 20))
tree.plot_tree(dtc, filled=True,
               feature_names=['attack', 'defense', 'magic', 'difficulty'],
               class_names=['fighter', 'mage', 'tank', 'assassin', 'support', 'marksman'])
plt.savefig('tree.png')
plt.show()