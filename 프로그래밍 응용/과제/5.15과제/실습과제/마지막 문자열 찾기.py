def find_all_count(filename, x):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            
        indices = []
        idx = text.find(x)
        
        # 문자열이 나타나는 모든 인덱스 찾기
        while idx != -1:
            indices.append(idx)
            idx = text.find(x, idx + 1)
            
        # result.txt에 결과 작성하기
        with open("result.txt", "w", encoding="utf-8") as out_file:
            if len(indices) > 0:
                # 1. 위치 인덱스 출력
                positions = "at " + ", ".join(map(str, indices)) + ".\n"
                out_file.write(positions)
                
                # 2. 빈도수 출력
                count_str = f"{len(indices)} time(s).\n"
                out_file.write(count_str)
            else:
                # 문자열이 없을 때
                out_file.write("not found")
                
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


find_all_count('article.txt','computer')
find_all_count('article.txt','Whole Earth')
find_all_count('article.txt','Apple')
find_all_count('article.txt','commencement')
find_all_count('article.txt','apple')
