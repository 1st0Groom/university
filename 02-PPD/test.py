def minsteps(n):
    steps = 0
    while n > 1:
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        steps += 1
    return steps

def run_minsteps(n):
    from time import perf_counter
    start = perf_counter()
    answer = minsteps(n)
    finish = perf_counter()
    print("minsteps(", n, ") => ", answer, sep="")
    print(round(finish-start), "seconds")

# Test code
run_minsteps(10)    # 3
run_minsteps(23)    # 6
run_minsteps(237)   # 8
run_minsteps(317)   # 10
run_minsteps(514)
run_minsteps(711)
run_minsteps(908)