def btod(d):
    d1=d[::-1]
    #n=0
    decno=0
    for i in range(len(d)):
        for j in d1:
            #n+=int(j)
            decno+=int(j)*(2**i)
            #n=0
    return decno

print(btod('0111'))