import pandas as pd

data = pd.read_csv('employee_salaries.csv')

department_summary = data.groupby('Department').agg({'Salary': 'sum', 'Bonus': 'mean'})
print(department_summary)

sorted_data = data.sort_values(by='Salary', ascending=False)
highest_salary_employee = sorted_data.iloc[0]
lowest_salary_employee = sorted_data.iloc[-1]
print("薪资最高的员工：")
print(highest_salary_employee)
print("\n薪资最低的员工：")
print(lowest_salary_employee)

department_range = data.groupby('Department')['Salary'].max() - data.groupby('Department')['Salary'].min()
print(department_range)

max_salary_employee_by_department = data.groupby('Department').apply(lambda x: x.loc[x['Salary'].idxmax()])
result_df = pd.DataFrame(max_salary_employee_by_department)
print(result_df)