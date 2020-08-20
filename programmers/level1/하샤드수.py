def solution(x):
    answer = False
    number = x
    num_list = []
    while x > 0:
        num_list.append(x%10)
        x //= 10
    if number % sum(num_list) == 0:
        answer = True
    return answer


if __name__ == '__main__':
    print(solution(10))
