#check the no is prime or not using for loop
p=int(input('enter num'))
for i in range(2,p):
    if p%i==0:
        print('composite')
        break
else:
    print('prime')

#using while loop
f=int(input('enter num'))
flag=True
i=2
while i<f:
    if f%i==0:
        flag=False
        break
    i+=1
else:
    print('prime')
if flag==True:
    print('composite')

# print('composite')



#using function
def prime(c):
    p,c1='prime','composite'
    for i in range(2,c):
        if c%i!=0:
            return p
        else:
            return c1
print(prime(10))

#using comprehension
# c=int(input('enter num'))
# res=[print('prime') if c%i!=0 else print('composite') for i in range(2,c)]
# print(res)