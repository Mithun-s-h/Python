#to encode the given string (en=ghiabcd)
def encode(s):
    en=''
    for i in s:
        if ord(i) in range(119,123):
            en+=(chr(ord(i)-22))
        else:

            en+=(chr(ord(i)+6))
    return en
print(encode('abcwxyz'))