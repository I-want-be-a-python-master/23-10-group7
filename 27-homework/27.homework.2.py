import pandas as pd
data = pd.read_csv("data_standardization.csv")
data['Price'] = data['Price'].str.replace('[$, USD]', '', regex=True).astype(float)
data = data.replace('None',0)
data['Total_Value']  =data.Price*data.Quantity
data.head(10)
data[['Category','Price']].groupby(by='Category').mean()
data[['Total_Value','Category']].groupby(by='Category').sum()