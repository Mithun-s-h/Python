# s='Happy New  Year Everyone'.split()
# d={}
# for i in s:
#     d[i]=i[::2]
# print(d)

a=input('enter the string')
out={}
for ch in a:
    if ch.isupper() and (ord(ch))%2==0:
        out[ch]=ord(ch),ch
    elif ch.isupper():
        out[ch]=ord(ch)
    elif ch.islower():
        out[ch]=ch
print(out)