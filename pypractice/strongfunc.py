def fact(n,res=1):
    for i in range(1,n+1):
        res*=i
    return res

def strong(n1,res1=0):
    # temp=n1
    for k in str(n1):
        res1+=fact(int(k))
    # while n1>0:
    #     ld=n1%10
    #     res1+=fact(ld)
    #     n1//=10
    if n1==res1:
        return True
    return False
print(strong(145))


