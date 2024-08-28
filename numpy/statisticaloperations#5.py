import numpy as np
s=np.array([10,20,30,50,80,100])

#1. max() : returns maximum value
print(np.max(s))

#2 min() : returns minimum value
print(np.min(s))

#3 sum() : returns total/sum of all elements in an array
print(np.sum(s))

#4 mean() : returns sum/total no of elements
print(np.mean(s))

#5 median() : sort's and return middle value.if 2 values then it'll sum then divided by 2
print(np.median(s))

#6 prod() : product/multiply all the elements
print(np.prod(s))

#7 std() :square root -sums and finds square root
print(np.std(s))

#8 var() :variance -finds median 
print(np.var(s)) #((median-value1)**2+.....(median-valuen)**2)/no of elements

