# 내 풀이
def solution(n):
    answer = ''
    while n:
        n, a = divmod(n, 3)
        answer = "412"[a] + answer
        if not a:
            n -= 1
    return answer


# 다른 사람 풀이
def change124(n):
    num = ['1', '2', '4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
