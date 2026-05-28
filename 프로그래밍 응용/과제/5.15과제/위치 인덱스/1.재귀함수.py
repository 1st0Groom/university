def 검색(s,x):
    def 반복(s,i):
        if s != []:
            if s[0] == x:
                return i
            else:
                return 반복(s[1:],i+1)
        else:
            return None
    return 반복(s,0)
    
print(검색([1,2,3,4,5],3))