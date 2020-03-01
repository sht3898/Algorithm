def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if not s[i].isdigit():
                answer = False
                break
    else:
        answer = False
    return answer