def solution(n):
    temp = ''
    while n > 0:
        temp += str(n % 3)
        n = n // 3
    return int(temp, base=3)


if __name__ == '__main__':
    print(solution(45)) # 7
    print(solution(125))    # 229
