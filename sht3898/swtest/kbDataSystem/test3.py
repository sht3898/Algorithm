# 달팽이가 우물을 탈출할 수 있는지 파악하는 문제
# 달팽이는 매일 기존의 갈 수 있는 거리*피로도만큼 갈 수 있는 거리가 줄어듦
# 우물을 탈출하면 Success 탈출에 걸린 일수 출력
# 우물 탈출 실패하면 Failure 0m로 돌아오는데 걸린 일수 출력

import sys
sys.stdin = open('test3_input.txt', 'r')


def escape(height, days):
    global result, U, day
    height += U
    U -= minus
    if height < 0:
        result = 'Failure'
        day = days
        return
    if height >= H:
        result = 'Success'
        day = days
        return
    escape(height-D, days+1)


H, U, D, F = 6, 2, 1, 10   # H: 우물높이, U: 달팽이가 하루에 갈 수 있는 거리, D: 자는 동안 미끄러지는 거리, F:피로도
# H, U, D, F = map(int, input().split())
result = 'Failure'
day = 1
minus = U * F * 0.01
escape(0, day)
print(result, day)
