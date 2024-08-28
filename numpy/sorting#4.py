import numpy as np
# sorting 1d array
a1=np.array([20,5,8,9,0,12])
print(np.sort(a1)) #by default sorting will be in ascending order
print(np.sort(a1)[::-1]) #for decending order reverse slicing

#  argsort() : it will sort the elements and returns their index nos as output
print(np.argsort(a1))

# sorting 2d array
a=np.array([[2,4,5],[1,3,6],[9,7,8]])
print(np.sort(a,axis=1)) #by default sort will be row wise axis=1
print(np.sort(a,axis=0)) #for column wise sort axis=0

# argument sort: argsort() -it will sort the elements and returns their index nos as output
print(np.argsort(a))
print(np.argsort(a,axis=1)) #by default sort will be row wise axis=1
print(np.argsort(a,axis=0)) #for column wise sort axis=0

#inplace sort : sorting and storing in the same memory loction or same variable
a=np.sort(a)
print(a)
a=np.argsort(a)
