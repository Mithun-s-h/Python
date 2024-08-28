# Indexing: a method to access/fetch and manupulate/operate data from array

# indexing on 1d array
import numpy as np
array1=np.array([10,20,30,'hello',50])
print(array1[0])
print(array1[3])

# indexing on 2d array
array2=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(array2)
print(array2[1,2])
print(array2[3,0])
print(array2[1,:])#row
print(array2[:,2])#column


# slicng on array : process of extracting a subset or a particular part of data from numpy array
# slicing on 1d array
array3=np.array([10,20,30,40,50,60])
print(array3[0:3])
print(array3[0:5:2])
print(array3[-1:-6:-1]) #negative indexing

# slicing on 2d array
# syntax: var[rowstart:rowend,columnstart:columnend]
array4=np.array(range(1,21)).reshape(4,5)
# print(array4)
print(array4[1]) #entire 1 indexed row
print(array4[:,0]) #entire 0 indexed column
print(array4[1:3,2:3])
print(array4[0:5,0:4])



