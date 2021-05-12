import pandas as pd

# creating a series using number default index
l=[1,1,3,4,6,7,7,8,'pratik']

# creating a series using our own index
p = {'data1':'1', 'data2':'2', 'data3': 'three'}

print(pd.Series(l))
print(pd.Series(p))

# creating frame using default index
df = [[1,2.2,-1,'data1'],['pratik',1,0.06],[-5,3443.3,'data2']]
print(pd.DataFrame(df))

# creating frame using custom index
print(pd.DataFrame(df,columns=['a','b','c','d'],index=[1,2,3]))

# creating dataFrame using directory
df1 = {'a':[1,2.2,-1,'data1'],'b':[1,2.2,-1,'data3']}
print(pd.DataFrame(df1))

print(pd.DataFrame(df).info())