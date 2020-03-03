import sys; sys.stdin = open('5432_input.txt', 'r')

for TC in range(1, int(input())+1):
    arr = input()
    stack = []
    result = 0
    for token in arr:
        if token == '(':
            stack.append(token)
            last = token
        else:
            stack.pop()
            if last == '(':
                result += len(stack)
                last = token
            else:
                result += 1
    print('#{} {}'.format(TC, result))
