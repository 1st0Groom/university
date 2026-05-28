def seq_search(s,x):
    def loop(i):
        for i in range(len(s)):
            if s[i] == x:
                return i
        return None

    return loop(0)

# Test code
print(seq_search([3, 5, 4, 2], 4))
print(seq_search([3, 5, 4, 2], 6))