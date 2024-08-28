#program to reverse all the list items
def rev(s):
    out=[]
    for i in s:
        out.append(i[::-1]) #to reverse the list out.append(s(i[::-1]))
    return out
print(rev(['123','hai','hello']))    

#to reverse list items and entire list
def rev1(l):
    out1=[]
    l=l[::-1]
    for j in l:
        out1.append(j[::-1])
    return out1
print(rev1(['123','hai','hello']))    

s=input('enter string')
res=''
for i in s:
    res=i+res
print(res)