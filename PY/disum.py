#digit sum using for loop
n=int(input('enter num'))
sum=0
for i in range(n):
    ld=n%10
    sum+=ld
    n=n//10
print(sum)

#digit sum usig while loop
x=int(input('enter num'))
sum=0
while x!=0:
    ld=x%10
    sum+=ld
    x//=10
print(sum)