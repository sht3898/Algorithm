import sys; sys.stdin = open('4831_input.txt', 'r')

for TC in range(1, int(input())+1):
    K, N, M = map(int, input().split()) # K: 최대 이동 정류장수, N: 종점 정류장, M: 충전기 설치 정류장
    stations = list(map(int, input().split()))
    result = 0
    now = 0
    battery = K
    for next_station in stations:
        if next_station - now > K:
            result = 0
            break
        if next_station - now > battery:
            battery = K
            result += 1
        battery -= next_station - now
        now = next_station

    if N - now > K:
        result = 0
    else:
        if N - now > battery:
            battery = K
            result += 1
        else:
            battery -= N - now
    print('#{} {}'.format(TC, result))
