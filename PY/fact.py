#to find factorial of a num6
n=int(input('enter num'))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

#using while loop
x=int(input('enter num'))
fac=1
k=1
while k<=x:
    fac*=k
    k+=1
print(fac)
#using while loop without initialize and updation of looping variable
f=int(input('num'))
fact=1
while f>0:
    fact*=f
    f=f-1
print(fact)

#using recursion

def fact_re(n,f=1):
    if n<=0:
        return f
    f*=n
    return fact_re(n-1,f)
print(fact_re(5))
