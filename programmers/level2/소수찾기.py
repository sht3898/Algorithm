from itertools import permutations


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    result = set([int(n) for n in numbers])

    for i in range(2, len(numbers) + 1):
        num = list(permutations(numbers, i))
        for n in num:
            if len(n) <= len(numbers):
                result.add(int(''.join(n)))
    result = list(result)

    if result.count(0):
        result.remove(0)
    if result.count(1):
        result.remove(1)

    for r in result:
        i = 2
        while i * i <= r:
            if r % i == 0:
                answer -= 1
                break
            i += 1
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution('17'))   # 3
    print(solution('011'))  # 2
