import matplotlib.pyplot as plt
import numpy as np
data = np.load('data\clean_lol_data_add_col.npy')


#统计数据
# 统计职业数量

values_pie=[0]*6
labels_pie=['fighter','mage','tank','assassin','support','marksman']
for roles in data[:,2:4].flat:
    if roles==labels_pie[0]:
        values_pie[0]+=1
    elif roles==labels_pie[1]:
        values_pie[1]+=1
    elif roles==labels_pie[2]:
        values_pie[2]+=1
    elif roles==labels_pie[3]:
        values_pie[3]+=1
    elif roles==labels_pie[4]:
        values_pie[4]+=1
    elif roles==labels_pie[5]:
        values_pie[5]+=1
print(values_pie)

#统计上手难度
index_bar=['D','C','B','A','S']
index_bar=['Level.'+str(index_bar[k]) for k in range(len(index_bar))]
values_bar=[0]*5
for j in data[:,8:].flat:
    j =j.astype(np.int32)
    if j>=9:
        values_bar[4]+=1
    elif j>=7:
        values_bar[3]+=1
    elif j>=5:
        values_bar[2]+=1
    elif j>=3:
        values_bar[1]+=1
    else:
        values_bar[0]+=1
print(values_bar)

#———绘图———
# 绘制饼状图
colors_pie=['#F7A6AC','#F7B7D2','#EEC186','#EEF0A7','#B2DBB9','#B8E5FA']#颜色
explode=[0.05,0.15,0.05,0.05,0.05,0.05]#分隔，突出最大部分

plt.title("Roles ratio",fontsize=25)
plt.pie(values_pie,labels=labels_pie,explode=explode,colors=colors_pie,
        startangle = 90,
        shadow=True,autopct='%1.1f%%')
plt.axis('equal')
plt.savefig('pic/roles_ratio.png')
plt.show()

#绘制柱状图
colors_pie=['#F7A6AC','#F7B7D2','#EEC186','#EEF0A7','#B2DBB9','#B8E5FA']#颜色

plt.title("difficulty distribution",fontsize=25)
plt.bar(index_bar,values_bar)
plt.savefig('pic/diff_distribution.png')
plt.show()