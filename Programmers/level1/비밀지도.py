def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        a = str(bin(a1 | a2)[2:])
        a = '0' * (n-len(a)) + a
        a = a.replace('1', '#')
        a = a.replace('0', ' ')
        answer.append(a)
    return answer


if __name__ == '__main__':
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
