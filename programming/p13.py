n=int(input('rows and columns'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j== n or j==1:
#             print('*',end='\t')
#         else:
#             print(' ',end='\t')
#     print()
        

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j==n+1:
#             print('|',end='\t')
#         else:
#             print('0',end='\t')
#     print()
        

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>j:
#             print('$',end='\t')
#         elif i<j:
#             print('@',end='\t')
#         else:
#             print(' ',end='\t')
#     print()

# $               @       @       @
# $       $               @       @
# $       $       $               @
# $       $       $       $

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==n//2+1 or j==n//2+1:
#             print('$',end='\t')
#         else:
#             print(' ',end='\t')
#     print()

#     $
#     $
# $ $ $ $ $
#     $
#     $


# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j== n or j==1:
#             print('*',end='\t')
#         elif i==j:
#             print('*',end='\t')
#         elif i+j==n+1:
#             print('*',end="\t")
#         else:
#             print(' ',end='\t')
#     print()

# *       *       *       *       *
# *       *               *       *
# *               *               *
# *       *               *       *
# *       *       *       *       *
# c=2
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>j:
#             print(c,end='\t')
#             c+=1
#         else:
#             print(' ',end='\t')
#     print()

c=65
for i in range(n):
    for j in range(n):
        if i>j or i==j:
            print(chr(c),end='\t')
            c+=1
        else:
            print(' ',end='\t')
    print()
