def solution(s, n):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    N = len(lower)
    answer = ''
    for c in s:
        for i in range(N):
            if c == lower[i]:
                answer += lower[(i+n)%N]
                break
            elif c == upper[i]:
                answer += upper[(i+n)%N]
                break
            elif c == ' ':
                answer += ' '
                break
    return answer
