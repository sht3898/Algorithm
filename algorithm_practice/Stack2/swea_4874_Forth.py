import sys
sys.stdin = open('4874_input.txt', 'r')

for TC in range(1, int(input())+1):
    arr = list(input().split())
    result = []
    check = 0
    for idx in arr:
        if idx not in ['+', '-', '*', '/']:
            result.append(idx)
        else:
            try:
                second = int(result.pop())
                first = int(result.pop())
                if idx == '+':
                    result.append(first+second)
                elif idx == '-':
                    result.append(first-second)
                elif idx == '*':
                    result.append(first*second)
                # elif idx == '/':
                else:
                    result.append(first//second)
            except:
                check = 1
    result.pop()
    if check or len(result) > 1:
        print('#{} {}'.format(TC, 'error'))
    else:
        print('#{} {}'.format(TC, result[0]))
