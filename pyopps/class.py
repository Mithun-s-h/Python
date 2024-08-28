class a:
    a=10
    b=20
    def __init__(self,name,phno,addr): #init method to initialize object members
        self.name=name
        self.phno=phno
        self.addr=addr
    def display(self): #method to access object methods
        print(a1.name,a1.phno,a1.addr)
    # @classmethod
    def show(cls): #method to access cls methods
        print(cls.a,cls.b)
a1=a('mithin',90090,'xyz') #creating object
print(a1.name,a1.phno,a1.addr) #accessing object members
a1.display()
a.a=20 #modifying class member
a1.name='sahana'#modifying object member
print(a1.name,a1.phno,a1.addr)
a1.show();