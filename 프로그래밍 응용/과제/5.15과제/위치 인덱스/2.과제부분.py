def seq_search(s, x):
    def loop(i):
        # i가 리스트 s의 길이보다 작을 때 (인덱스 범위 내에 있을 때)
        if i < len(s):
            if s[i] == x:
                return i         # 값을 찾으면 인덱스 반환
            else:
                return loop(i+1) # 값을 못 찾으면 다음 인덱스로 재귀 호출
        else:
            return None          # 끝까지 못 찾으면 None 반환
    return loop(0)

# Test code
print(seq_search([3, 5, 4, 2], 4))
