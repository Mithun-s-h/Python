import pandas as p
df=p.read_csv('C://Users//mithu//OneDrive//Desktop//python//pandas//df.csv')
print(df)
# selecting a single row:
print(df.loc[0])
print(df.iloc[0,4])# indexing[row,element]
print(df.iloc[0:4])#slicing on DF

# selecting a single columns 
print(df['age'])
# selecting multiple columns
print(df[['name','age']])

# filter rows
print([df['age']>22])



