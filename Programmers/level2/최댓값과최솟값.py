def solution(s):
    result = list(map(int, s.split()))
    return f'{min(result)} {max(result)}'


print(solution('1 2 3 4'))  # 1 4
print(solution('-1 -2 -3 -4'))  # -4 -1
print(solution('-1 -1'))    # -1 -1
