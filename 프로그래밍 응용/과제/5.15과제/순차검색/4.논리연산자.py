def 순차검색(s,x):
    return s != [] and (s[0] == x or 순차검색(s[1:], x))

print(순차검색([3,4,2,5], 2))



