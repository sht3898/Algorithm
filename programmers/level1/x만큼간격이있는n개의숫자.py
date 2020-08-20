def solution(x, n):
    answer = []
    number = x
    while len(answer) != n:
        answer.append(number)
        number += x
    return answer


def solve(x, n):
    return list(x+x*i for i in range(n))


if __name__ == '__main__':
    print(solution(2, 5))
    print(solve(2, 5))
