import numpy as np
# 1d array

list1=[10,20,30,40,50]
# array1=np.array(list1)#.reshape(5,1)
# print(array1)

# # exlpicit declaration of datatype

# array1=np.array(list1,dtype=float)#can be any datatype
# print(array1)

# # 2d array

# list2=[[10,20,30],[40,50,60],[70,80,90]]
# array2=np.array(list2)
# print(array2)

# # creating by using range (arange)

# array3=np.arange(1,20,2)
# print(array3)

# # 2d using reshape()

# array4=np.arange(10,22).reshape(4,3)
# print(array4)

# # creatin array with 0's and 1's :always returns in floa
array5=np.zeros(5)
array6=np.ones((5,2)) #n dimentional 
# print(array5)
print(array6)

# # Attributes of numpy array


# 1. ndim : no of dimentions
#print(array6.ndim)

# # 2. shape : no of rows and columns
# print(array6.shape)
  
# # 3. size : total no of elements
# print(array6.size)

# # 4. dtype : specifies the type of data
# print(array6.dtype)

# # 5. itemsize : size of each element (in bytes)
# print(array6.itemsize)




