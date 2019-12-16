import sys
sys.stdin = open('14889_input.txt', 'r')


def perm(k, n):
    global result
    if k == N:
        return
    if n == N // 2:
        st_team, li_team = [], []
        for i in range(N):
            if visit[i]:
                st_team.append(i)
            else:
                li_team.append(i)
        s, l = 0, 0
        for i in range(N // 2):
            for j in range(i+1, N//2):
                s += arr[st_team[i]][st_team[j]] + arr[st_team[j]][st_team[i]]
                l += arr[li_team[i]][li_team[j]] + arr[li_team[j]][li_team[i]]
        tmp = abs(s - l)
        result = min(result, tmp)

    visit[k] = 1
    perm(k+1, n+1)
    visit[k] = 0
    perm(k+1, n)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [0] * 20
result = 0xffff
perm(0, 0)
print(result)
