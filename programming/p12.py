# n=int(input('enter the no of rows and columns'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(str(i)+str(j),end='\t')
#     print()

n=int(input('enter the no of rows and columns'))
# for i in range(1,n+1):
#     print(' '*i +'*')

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == j:
#             print('*')
#         else:
#             print(' ',end='\t')
#     print()

# for i in range(1,n+1):
#     print('*'*i )

# for i in range(1,n+1):
#     print(' '*i +(n-i)*'*')

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i > j:
#             print('*',end=' ')
#         elif i==j:
#             print('@',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i < j:
#             print('!',end=' ')
#         elif i==j:
#             print('$',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1:
#             print(str(i)+str(j),end='\t')
#         else:
#             print(' ',end='\t')
#     print()

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1:
#             print('*',end='\t')
#         else:
#             print(' ',end='\t')
#     print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n:
            print('*',end='\t')
        elif i+j==n+1 and i>n%3 or j==i and i>n%3:
            print('*',end='\t')
        else:
            print(' ',end='\t')
    print()





