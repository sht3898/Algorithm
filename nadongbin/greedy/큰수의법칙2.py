# N(배열의 크기), M(숫자가 더해지는 횟수), K(연속해서 더해질 수 있는 수)를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
data = [2, 4, 5, 4, 6]
n, m, k = 5, 8, 3

data.sort()
first = data[n-1]
second = data[n-2]

cnt = int(m/(k+1)) * k
cnt += m % (k+1)

result = 0
result += cnt * first
result += (m-cnt) * second

print(result)
