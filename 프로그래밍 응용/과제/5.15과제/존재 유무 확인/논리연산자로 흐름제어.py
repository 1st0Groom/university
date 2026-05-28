def bin_search_OX(ss,x):
    mid = len(ss) // 2
    return ss != [] and \
        (x == ss[mid] or \
            ss[mid] < x and bin_search_OX(ss[mid+1:], x) or \
            ss[mid] > x and bin_search_OX(ss[:mid], x))

s = [3,5,8,7,4,6,1,9,2]
s.sort()
print(bin_search_OX(s,5))
print(bin_search_OX(s,8))
print(bin_search_OX(s,1))
print(bin_search_OX(s,11))