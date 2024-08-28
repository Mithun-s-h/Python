# Arithematic operations on numpy array
#  size of both array should be same or equal
import numpy as np
array1=np.array([[10,20,30],[40,50,60],[70,80,90]])
array2=np.array([[70,80,90],[40,50,60],[10,20,30]])
# 1. Addition (+) :
print(array2+array1)

#2. substraction (-) :
print(array2-array1)

#3. multiplication (*) :
mul=array2*array1 #assigning to a variable
print(mul)

#4. matrix multiplication (@) :
print(array1@array2)

#5. division (/): always returns in floting point/float value
print(array2/array1)

#6. floor division (//): always returns integer value
print(array2//array1)

#7. exponentiation (**): powering
print(array2**5)
print(array1**array2)

#8. module (%):returns remainder
print(array2%array1)

#9. transpose() : inter change of rows and columns
print(array1.transpose())
