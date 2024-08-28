ip='hai hello how are you'
c=0
# for i in ip:
#     if i==' ':
#         c+=1
# op=ip.replace(' ','_')
op=ip.replace(' ','_')
print(ip+str(ip.count(' ')**2))





out=''
for i in ip:
    if i==' ':
        out+='_'
        c+=1
    else:
        out+=i

print(out+str(c*c))




