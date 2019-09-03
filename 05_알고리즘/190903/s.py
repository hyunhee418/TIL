a = 11213
def mono(a):
    i = 0
    while  (a // 10**(i+1)) % 10 != 0:
        if (a // 10**(i)) % 10 < (a // 10**(i+1)) % 10:
            return False
        i += 1
    return True
print(mono(a))