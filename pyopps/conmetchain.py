class A:
    a=10 #generic states
    b=20
    def __init__(self,p,q):
        self.p=p #specific states
        self.q=q
    def display(self):
        print(self.p,self.q)
class B(A):
    c=10
    def __init__(self,p,q,r):
        super().__init__(p,q)
        self.r=r
    def display(self):
        super().display() 
        print(self.r)
obj1=B(10,20,30)
obj1.display()
# print(help(obj1))
print(B.mro())
print(obj1.__dict__)