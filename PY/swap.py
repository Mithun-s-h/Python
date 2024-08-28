#to swap to nos based on position
def swap(lst, pos1, pos2):
    tmp = lst[pos1-1]
    lst[pos1-1] = lst[pos2-1]
    lst[pos2-1] = tmp
    return lst

x=eval(input('Enter a list: '))
p1 = int(input('Enter first position: '))
p2 = int(input('Enter second position: '))
print(swap(x,p1,p2)) 
