import sys
sys.stdin = open('4874_input.txt', 'r')

for TC in range(1, int(input())+1):
    arr = list(input().split())
    result = []
    meet = 0
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
                meet = 1
    result.pop()
    if meet or len(result) > 1:
        print('#{} {}'.format(TC, 'error'))
    else:
        print('#{} {}'.format(TC, result[0]))
