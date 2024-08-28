import pandas as p
df=p.read_csv('C://Users//mithu//OneDrive//Desktop//python//pandas//df.csv')

# 1. head():by default it'll dispaly top 5 rows
print(df.head(2))

# 2.tail(): by default it'll dispaly last 5 rows
print(df.tail(2))

# 3.shape :displays no of rows and columns in a DF
print(df.shape)

# 4.columns :list of columns names
print(df.columns)
print(df.age) #it'll display full 'age' column data

# 5.size: no of rows * no of columns
print(df.size)

# 6.dtypes: displays datatype of each column
print(df.dtypes)

# 7. values:converts all the values into an array format
print(df.values)

# 8 .index:shows the index 
print(df.index)

