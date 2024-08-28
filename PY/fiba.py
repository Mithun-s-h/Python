#fibanocci series
def fib(f):
    out=[]
    # f1=range(f+1)
    for i in range(1,f+1):
        for j in range(1,f+1):
            if i==f[j-1]+f[j-2]:
                out+=i
    return out
print(fib(10)) 
