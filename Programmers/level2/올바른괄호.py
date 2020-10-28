def solution(s):
    cnt = 0
    for idx, value in enumerate(s):
        if idx == 0:
            if value == ')':
                return False
        if value  == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return cnt == 0


if __name__ == '__main__':
    print(solution("()()")) #t
    print(solution("(())()"))   #t
    print(solution(")()(")) #f
    print(solution("(()(")) #f
