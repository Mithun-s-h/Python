import pickle

# pickling
py_data=['mithun','jin','ak']
fileobj=open('pickle.pkl','wb')
pickle.dump(py_data,fileobj)
fileobj.close()

# unpickling

fileobj1=open('pickle.pkl','rb')
py_data1=pickle.load(fileobj1)
print(py_data1)
fileobj1.close()
