def solution(n):
    def binary(number):
        temp = ''
        while number > 0:
            temp += str(number % 2)
            number = number // 2
        return temp[::-1]

    n_cnt = binary(n).count('1')
    idx = n + 1
    while idx <= 1000000:
        bin_num = binary(idx)
        bin_cnt = bin_num.count('1')
        if n_cnt == bin_cnt:
            return idx
        else:
            idx += 1


def solution2(n):
    bin_n = bin(n).count('1')
    for i in range(n+1, 1000001):
        if bin_n == bin(i).count('1'):
            return i


print(solution(78)) # 83
print(solution(15)) # 23
print(solution2(78)) # 83
print(solution2(15)) # 23
