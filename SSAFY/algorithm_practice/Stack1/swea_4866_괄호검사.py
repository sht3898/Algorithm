import sys
sys.stdin = open('4866_input.txt', 'r')

for TC in range(1, int(input())+1):
    arr = list(input())
    result = []
    ans = 1
    for idx in arr:
        if idx in ['(', '{']:
            result.append(idx)
        elif idx in [')', '}']:
            if len(result) == 0:
                ans = 0
                break
            if idx == ')' and result[-1] == '{':
                ans = 0
                break
            if idx == '}' and result[-1] == '(':
                ans = 0
                break
            result.pop()
    if len(result):
        ans = 0
    print('#{} {}'.format(TC, ans))
