#to extract all palindrome strings in a collection

def is_pal(s,i=0,out=[]):
    # out=[]
    if i>=len(s):
        return out
    if s[i]==s[i][::-1]:
        out.append(s[i])
       

        print(s[i])
    return is_pal(s,i+1)

    


    
print(is_pal(['mom','hai','www','mim']))