# pandas store tabular data using DataFrame
# DataFrame: is a 2D labelled data structure like 'table' in DB
# every DF contains 'rows' and 'columns' and has their own index no
# each column can have a different type of data

# creating an DF :2 methods
# 1. Manual method:
import pandas as p
st_data=[(1,'mithun',21,'male','skp'),
         (2,'san',22,'female','anv'),
         (3,'jin',23,'male','srkp'),
         (4,'ak',22,'male','skp')]
df=p.DataFrame(st_data,columns=['id','name','age','gender','addr'])
print(df) 

#2. using csv file:
# df1=p.read_csv('df.csv')
df2=p.read_csv('C://Users//mithu//OneDrive//Desktop//python//pandas//df.csv')
print(df2)
