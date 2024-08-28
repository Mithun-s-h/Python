# method: a function which is defined inside the class 
# 3types 
# 1.class method: method to access and modify members of a class
# 2.object method: method to access and modify members of a object
# 3.static method: supports a class or object method

# 1. class method:
class library:
    name='ABC'
    loc='skp'
    head='XYZ'
    def __init__(self,vid,vname,vphno,nob):
        self.vname=vname
        self.vid=vid
        self.vphno=vphno
        self.nob=nob
    @classmethod
    def show_class(cls):
        print(cls.name,cls.loc,cls.head)

    @classmethod
    def modify_name(cls,new):
        cls.name=new
    
    @classmethod
    def modify_head(cls,new):
        cls.head=new

    def show(self):
        print(self.vname,self.vid,self.vphno,self.nob)
    def modify_vphno(self,new):
        self.vphno=new
library.modify_head('YYY') #modify
library.show_class() #access



#2. object method:



v1=library('mithun',1,9353362598,5)
v2=library('san',2,9353362598,10)

v1.modify_vphno(123456789) #modify
v1.show() #acessing

# print(help(v2))

# print(library.mro())


