l=eval(input('enter the list'))
even=[]
odd=[]
for value in l:
    if value%2==0:
        even.append(value)
    else:
        odd.append(value)
if sum(even)>sum(odd):
    print(even)
else:
    print(odd)