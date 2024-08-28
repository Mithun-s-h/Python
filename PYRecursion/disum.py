def digit_sum(n,sum=0):
    if n<=0:
        return sum
    sum+=n%10
    n//=10
    return digit_sum(n,sum)
print(digit_sum(12345))
