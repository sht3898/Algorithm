# N(배열의 크기), M(숫자가 더해지는 횟수), K(연속해서 더해질 수 있는 수)를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
data = [2, 4, 5, 4, 6]
n, m, k = 5, 8, 3

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
