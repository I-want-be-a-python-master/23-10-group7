import pandas as pd

df = pd.read_csv("data_transformation.csv")
df[['First_Name', 'Last_Name']] = df['Full_Name'].str.split(' ', expand=True)
df.drop(columns=['Full_Name'], inplace=True)

df['Join_Date'] = pd.to_datetime(df['Join_Date'])
current_date = pd.to_datetime('today')
df['Years_of_Service'] = (current_date - df['Join_Date']).dt.days // 365
print(df.head(12))

df['Performance_Score'] = (df['Performance_Score'] - 80) * 2
print(df.head(12))

manager_avg_score = df.groupby('Manager')['Performance_Score'].mean()
print(manager_avg_score)
