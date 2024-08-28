#swap first and last no in a list
def sfl(l):
    s=[]
    temp=l[0]
    l.pop(0)
    temp1=l[len(l)-1]
    l.pop(len(l)-1)
    l.insert(0,temp1)
    l.insert(len(l),temp)
    return l
  
print(sfl([1,2,3,4]))