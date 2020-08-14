def solution(s):
    answer = ''
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    N = len(s)
    M = len(lower)
    for i in range(N):
        if i % 2 == 0:
            if s[i] in upper or s[i] == ' ':
                answer += s[i]
            else:
                for j in range(M):
                    if s[i] == lower[j]:
                        answer += upper[j]
                        break

        else:
            if s[i] in lower or s[i] == ' ':
                answer += s[i]
            else:
                for j in range(M):
                    if s[i] == upper[j]:
                        answer += lower[j]
                        break
    return answer


if __name__ == '__main__':
    print(solution('try hello world'))
