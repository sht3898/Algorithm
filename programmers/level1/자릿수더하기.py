def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n //= 10
    return answer


def solution2(n):
    return sum(map(int, str(n)))


if __name__ == '__main__':
    print(solution(123))
    print(solution2(123))