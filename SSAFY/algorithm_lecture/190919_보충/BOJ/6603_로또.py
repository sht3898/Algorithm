import sys; sys.stdin = open('6603_input.txt')


def solve(k, s):
    if k == 6:
        print(*arr)
        return
    for i in range(s, len(S)):
        num = S[i]
        if not meet[i]:
            meet[i] = 1
            arr.append(num)
            solve(k+1, i)
            arr.pop()
            meet[i] = 0


while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    K, S = arr[0], arr[1:]
    meet = [0] * len(S)
    arr = []
    solve(0, 0)
    print()

