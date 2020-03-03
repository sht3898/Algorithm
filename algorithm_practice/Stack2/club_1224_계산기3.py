import sys; sys.stdin = open('1224_input.txt', 'r')

icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

for TC in range(1, 11):
    N = int(input())
    arr = list(input())
    stack = []
    numbers = []
    tokens = []
    for idx in arr:
        if idx.isdigit():
            numbers.append(idx)
        else:
            if not tokens:
                tokens.append(idx)
                continue
            else:
                if idx == ')':
                    while tokens[-1] != '(':
                        numbers.append(tokens.pop())
                    tokens.pop()
                elif icp[idx] > isp[tokens[-1]]:
                    tokens.append(idx)
                else:
                    while tokens and (icp[idx] <= isp[tokens[-1]]):
                        numbers.append(tokens.pop())
                    tokens.append(idx)

    for j in numbers:
        if j.isdigit():
            stack.append(j)
        else:
            num1, num2 = int(stack.pop()), int(stack.pop())
            if j == '+':
                stack.append(num1 + num2)
            elif j == '*':
                stack.append(num1 * num2)
    print('#{} {}'.format(TC, *stack))
