# # sql connection
# import sqlite3
# v1=sqlite3.connect('data.db')
# v2=v1.cursor()
# # v2.execute('create table student(name varchar(20),phno number)')
# v2.execute('insert into student values("mithun","10")')
# res=v2.execute('select * from student')
# print(list(res))
# v1.commit()
# v1.close()

# writing data into file
obj=open('text.txt','w')
obj.write('hai\n')
obj.writelines(['hai','hello','mithun'])  
obj.close()

# # reading data from file
# obj=open('text.txt','r')
# read=obj.readlines()
# print(read)
# obj.close()