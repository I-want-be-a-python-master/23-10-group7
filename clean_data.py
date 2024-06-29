# 解析数据-解析json
# 清洗数据-保存npy
import json
import numpy as np


with open('hero_list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    dic = data['hero']

# dic[0]['name'] # 英雄名称
# dic[0]['title'] # 中文名
# dic[0]['roles'] # 职业
# dic[0]['attack'] # 攻击
# dic[0]['defense'] # 防御
# dic[0]['magic'] # 魔力
# dic[0]['difficulty'] # 上手难度



# 按照（将同一英雄的职业展开,放在同一行————一列变多列）的方式处理数据

name = np.array([dic[i]['name'] for i in range(len(dic))])
title = np.array([dic[i]['title'] for i in range(len(dic))])
max_length = len(max([dic[i]['roles'] for i in range(len(dic))], key=len))
roles = np.array([(dic[i]['roles'] + [np.nan]*(max_length - len(dic[i]['roles']))) for i in range(len(dic))])
attack = np.array([dic[i]['attack'] for i in range(len(dic))])
defense = np.array([dic[i]['defense'] for i in range(len(dic))])
magic = np.array([dic[i]['magic'] for i in range(len(dic))])
difficulty = np.array([dic[i]['difficulty'] for i in range(len(dic))])
# 数组堆叠(列)
data = np.column_stack((name, title, roles, attack, defense, magic, difficulty))
# 保存数据
np.save('clean_lol_data_add_col.npy', data)


# 按照（将同一英雄的职业展开,放在同一列————一行变多行）的方式处理数据

old_data = np.load('clean_lol_data_add_col.npy')
# 将数组的每一行复制
new_data = np.repeat(old_data, repeats=3, axis=0)
# 将职业放在同一列
for i in range(0,len(new_data),3):
    new_data[i][2]
    new_data[i+1][2] = new_data[i][3]
    new_data[i+2][2] = new_data[i][4]
# 删除多余的职业列
new_data = np.delete(new_data, (3,4), axis=1)
# 删除职业列中包含有nan的行
new_data = new_data[new_data[:,2] != 'nan']
# 保存数据
np.save('clean_lol_data_add_row.npy', new_data)


# 去除多余的数据列，便于机器学习(只保留职业和属性)
l_data = np.load('clean_lol_data_add_row.npy')
l_data = np.delete(l_data, (0,1), axis=1)
# 保存数据
np.save('clean_lol_data.npy', l_data)