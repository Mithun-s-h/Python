def oddeven(l,i=0,e=0,o=0):
    if i>=len(l):
        
        return e,o
    if i%2==0:
        e+=l[i]
    o+=l[i]
    return oddeven(l,i+1,e,o)
print(oddeven([10,11,12,15,20]))