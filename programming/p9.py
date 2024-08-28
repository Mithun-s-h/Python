s=input('string')
ip=input('substr')
l=len(ip)
for i in range(len(s)):
    if s[i:l+i:]==ip:
        print(True)
        break
else:
    print(False)
# else:
    
#     print(False)
