import sys
sys.stdin = open('14501_input.txt', 'r')


def solve(date, money):
    global ans
    if date == N:  # 현재 날짜가 퇴사예정일 일때
        ans = max(ans, money)
        return
    # 상담가능한 날이 현재 날짜에서 퇴상예정일까지 남은 날보다 짧을 때
    if T[date] <= N - date:
        solve(date + T[date], money + P[date])
    solve(date + 1, money)


N = int(input())
T, P = [], []
ans = 0
for _ in range(N):
    tmp1, tmp2 = map(int, input().split())
    T.append(tmp1)
    P.append(tmp2)
solve(0, 0)
print(ans)
