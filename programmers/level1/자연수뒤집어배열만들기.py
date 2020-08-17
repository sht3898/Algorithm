def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    return answer[::-1]


def solution2(n):
    return list(map(int, str(n)))[::-1]


if __name__ == '__main__':
    print(solution(12345))
    print(solution2(12345))

