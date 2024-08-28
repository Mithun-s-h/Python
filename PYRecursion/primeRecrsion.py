def prime_r(n,i=2):
    res='prime'
    res1='not prime'
    if n<i:
        return
    if n%i==0:
        return res1
    return res
    return prime_r(n,i+1)

print(prime_r(6))
