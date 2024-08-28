# def prime(n,p=[]):
#     for i in range(1,n+1):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             p.append(i)
#     print(p)
# prime(10)

# to remove duplicates

# def remove(l,out=[]):
#     for i in l:
#         if l.count(i)==1:
#             out.append(i)
#     return(out)
# print(remove([1,1,2,3,4,5,5,6,7,8,8,9,9]))


# reverse the words in a given sentence

# def word(sentence,out=''):
#     for i in sentence.split():
#         out=i+' '+out
#     return out
# print(word('hai hello hwo are you'))


# def inter(l1,l2,out=[]):
#     for i in l1:
#         if i in l2 and i not in out:
#             out.append(i)
#     print(out)
# inter([1,2,2,5,3,4,5,6,7],[5,6,7,8,9,0])

# factoria of a number
# def rec(n,i=1,sum=1):
#     if i>n:
#         return sum
#     sum*=i
#     return rec(n,i+1,sum)
# print(rec(4))



text=open('text.txt','r')
f1=text.read()

l=list(f1.split())
d={i:l.count(i) for i in l}
print(d)

