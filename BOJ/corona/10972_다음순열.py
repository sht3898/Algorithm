import sys; sys.stdin = open('10972_input.txt', 'r')

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
x = 0

for i in range(n - 1, 0, -1):
    if s[i - 1] < s[i]:
        x = i - 1
        break
print("x값(순서를 바꿔야할 인덱스 번호) =", x)

for i in range(n - 1, 0, -1):
    if s[x] < s[i]:
        print("바꾸기 전 배열 = ", *s)
        s[x], s[i] = s[i], s[x]
        s = s[:x + 1] + sorted(s[x + 1:])
        print("바꾼 후 배열 = ", *s)
        exit()
print(-1)
