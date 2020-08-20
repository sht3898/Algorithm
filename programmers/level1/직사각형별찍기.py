def solution(number):
    a, b = map(int, number.strip().split(' '))
    for i in range(b):
        print('*'*a)


if __name__ == '__main__':
    solution('5 3')
