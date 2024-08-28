s=input('enter the string')
u,l,sp='','',''
for i in s:
    if i.isupper():
        u+=i
    elif i.islower():
        l+=i
    else:
        sp+=i
if len(s)==10:
    print(l)
elif len(s)<10:
    print(u)
else:
    print(sp)