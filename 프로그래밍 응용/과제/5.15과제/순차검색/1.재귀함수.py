def 순차검색(s,x):
    if s != []:
        if s[0] == x:
            return True
        else:
            return 순차검색(s[1:],x)
    else:
        return False

print(순차검색([3,5,4,2], 4))





















































































