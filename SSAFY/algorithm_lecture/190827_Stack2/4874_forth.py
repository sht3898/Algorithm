import sys; sys.stdin = open('4874_input.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    arr = list(input().split())
    stack = []
    meet = 0
    for i in range(len(arr)-1):
        if arr[i].isdigit():
            stack.append(arr[i])
        else:
            try:
                num2, num1 = int(stack.pop()), int(stack.pop())

                if arr[i] == '+': result = num1 + num2
                elif arr[i] == '-': result = num1 - num2
                elif arr[i] == '*': result = num1 * num2
                elif arr[i] == '/': result = num1 // num2

                stack.append(result)

            except:
                meet = 'error'

    if meet == 0 and len(stack) == 1:
        print('#{} {}'.format(tc, stack.pop()))

    elif meet == 'error' or len(stack) > 1:
        print('#{} error'.format(tc))
