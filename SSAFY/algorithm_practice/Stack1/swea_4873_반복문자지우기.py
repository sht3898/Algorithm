import sys
sys.stdin = open('4873_input.txt', 'r')

for TC in range(1, int(input())+1):
    arr = list(input())
    result = []
    for idx in arr:
        if not result or idx != result[-1]:
            result.append(idx)
        elif idx == result[-1]:
            result.pop()
    print('#{} {}'.format(TC, len(result)))
