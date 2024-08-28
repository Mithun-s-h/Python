#spilt and extract when encounter upper or lower case alphabets (slice there)
def alph(s):
    pair=[]
    w=''
    for i in range(len(s)-1):
        if ord(s[i])==ord(s[i+1])-1:
            w+=s[i]
        else:
            w+=s[i]
            pair.append(w)
            w=''
    w+=s[i+1]
    pair.append(w)
    return pair
print(alph('efgABmnopxpq'))
