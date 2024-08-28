def is_valid(st):
    if len(st)<8:
        return False
    else:
        for i in st:
            if i.isupper() and i.isdigit() and i.islower():
                if i in '@$&':
                     return True
                else:
                     return False
print(is_valid('Mithun@2005'))
