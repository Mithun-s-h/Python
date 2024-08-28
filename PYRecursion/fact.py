def rec_fact(n,fact=1):
#     if n>0:
#         sum*=n
#         return sum
#     n=n-1
#     return rec_fact(n,sum)
# print(rec_fact(10))
    
    if n<=0:
        return fact
    fact*=n
    n-=1
    rec_fact(n,fact)
print(rec_fact(10))

    