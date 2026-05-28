def find_2nd(filename, x):
    try:
        # 파일 내용을 읽어옵니다
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return None

    # 1. 첫 번째 x의 인덱스를 찾습니다
    first_idx = content.find(x)
    
    # 2. 첫 번째 위치를 찾았다면, 그 다음 인덱스부터 다시 탐색합니다
    if first_idx != -1: 
        second_idx = content.find(x, first_idx + 1)
        
        # 3. 두 번째 위치도 찾았다면 파일에 씁니다
        if second_idx != -1:
            with open("result.txt", "w", encoding="utf-8") as out_file:
                out_file.write(str(second_idx))
            print(f"at {second_idx} the 2nd time.")
            return second_idx

    # 4. 첫 번째를 못 찾았거나, 두 번째를 못 찾은 경우
    with open("result.txt", "w", encoding="utf-8") as out_file:
        out_file.write("not found.")
    print("not found.")
    return None

# Test code
find_2nd('article.txt','computer')    # at 3357 the 2nd time.
find_2nd('article.txt','Whole Earth') # at 11280 the 2nd time.
find_2nd('article.txt','Apple')       # at 4455 the 2nd time.
find_2nd('article.txt','apple')       # not found.