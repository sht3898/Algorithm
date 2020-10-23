def solution(numbers):
    l = []
    for number in numbers:
        original = str(number)
        number = list(str(number))
        i = 0
        while len(number) <= 4:
            number.append(original[i])
            i = (i + 1) % len(original)
        number = int("".join(number))
        l.append([number, original])

    l = sorted(l, reverse=True)
    return str(int("".join([item[1] for item in l])))


def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


if __name__ == '__main__':
    print(solution2([6, 10, 2])) # 6210
    print(solution([3, 30, 34, 5, 9]))  # 9534330
