def list2(l):
    l=[1,2,3,'hai',[1,2]]
    count=0
    i=0
    while i<len(l):
        if type(l[i])==type(l[i+1]):
            count+=1
            i+=1
    if count!=0:
        print(True)
    else:
        print(False)
        
    print(list2([1,2,3,'hii']))