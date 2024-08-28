#extract uppercase alpha
s=input('enter string')
i=0
u=''
l=''
while i<len(s):
    if 'A'<=s[i]<='Z':
        u+=s[i]
        i+=1
    else:
        l+=s[i]
        i+=1
print(u)
print(l)