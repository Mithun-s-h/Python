import pandas as p
df=p.read_csv('C://Users//mithu//OneDrive//Desktop//python//pandas//df.csv')

# adding a new column to DF 2 ways
# 1.
df['phno']=[111,222,333,444,555,666]

df['phno1']=111 # it'll add same no for all the rows

# 2.using insert(index no,col_name,values):
df.insert(3,'qualification',['bca','be','bca','bca','bca','Lkg'])

# deleting a column from df:
# df=df.drop(columns=['phno1'])
# or
del df['phno1']

# rename a column name
df=df.rename(columns={'qualification':'quali'})

# inserting a new row
df.loc[4]=[7,'pengu',22,'ukg','female','bnglr',777]

# deleting a row
# df=df.drop(4)

# updating the value
df.loc[4,'id']=5

# updating the value for multiple rows
df.loc[[4,5],'phno']=[666,777]
print(df)
