#extract all string from list which contains at least one vowel character
 
def vowel(s):
    out=[]
    for i in s:
        for j in i:
            if j in 'aeiouAEIOU':
                out.append(i)
    print(out)
vowel(['mit','jin','shx'])
