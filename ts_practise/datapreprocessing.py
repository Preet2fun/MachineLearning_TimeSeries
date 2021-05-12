import pandas as pd
from matplotlib import pyplot as plt

dataframe = pd.read_csv('daily-total-female-births-CA.csv', header=0)
#print(dataframe.head())
#print(dataframe['date'].dtype)

df = pd.read_csv('daily-total-female-births-CA.csv', header=0, parse_dates=[0])
#print(df.head())
#print(df['date'].dtype)

series = pd.read_csv('daily-total-female-births-CA.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
#print(series.head())
#print(series.dtype)

#print(series['1959-01'])
#print(df[(df['date'] > '1959-01-05') & (df['date'] < '1959-02-05')])

df2 = pd.read_csv('daily-total-female-births-CA.csv', header=0, parse_dates=[0])
print(df2.head())
df2.index = df2['date']
print(df2.head())

print(df2['births'].plot())