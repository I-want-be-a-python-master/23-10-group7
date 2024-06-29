import pandas as pd

# 读取数据集并计算每个部门的总工资和平均奖金。
df=pd.read_csv('employee_salaries.csv')
sum_salary=df.groupby('Department')['Salary'].sum()
mean_bonus=df.groupby('Department')['Bonus'].mean()
print(sum_salary)
print(mean_bonus)
# 按照Salary列对数据进行排序，并找出薪资最高和最低的员工。
df_sorted=df.sort_values(by='Salary',ascending=False)
highest_employee=df_sorted.iloc[0]
lowest_employee=df_sorted.iloc[-1]
print(highest_employee)
print(lowest_employee)
# 计算每个部门的薪资范围
department_ranges = df.groupby('Department')['Salary'].agg(['min', 'max']).reset_index()
department_ranges['Range'] = department_ranges['max'] - department_ranges['min']
print(department_ranges)

# 找出每个部门薪资最高的员工
top_salary_per_department = df.groupby('Department')['Salary'].transform(max) == df['Salary']
top_salary_df = df[top_salary_per_department].drop_duplicates(subset=['Department'])
print(top_salary_df)