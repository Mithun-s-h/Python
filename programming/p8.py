# print the second maximum score or runnerup
# score=eval(input('score'))
# print(sorted(score)[-2])

# m=0
# r=0
# for n in score:
#     if m<n:
#         r=m
#         m=n
# print(r)
# max=max(score)
# run=0
# for j in score:
#     if j<max and j>run:
#         run=j

# print(run)

# write a program to extract even digit from string which are present at even index and the ascii value is even
s=input('string')
out=''
for i in s:
    if i.index()%2==0 and ord(i)%2==0:
        out+=i
print(out)