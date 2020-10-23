# 풀이1
def solution(s):
    answer = True
    p_count = s.count('p') + s.count('P')
    y_count = s.count('y') + s.count('Y')
    print(p_count, y_count)
    if p_count != y_count:
        answer = False
    return answer

# 풀이2
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
