def 순차검색(s,x):
    for 키 in s:
        if 키 == x:
            return True
    return False

print(순차검색([3,5,4,2],4))