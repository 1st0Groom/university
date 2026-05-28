def 순차검색(s,x):
    while s != []:
        if s[0] == x :
            return True
        else:
            s = s[1:]
    return False

print(순차검색([3,5,4,2],4))



