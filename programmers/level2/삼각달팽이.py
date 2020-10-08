def solution(n):
    arr = [[0] * _ for _ in range(1, n + 1)]
    num = 1
    j = 0
    k = 0

    for i in range(1, n+1):
        # 왼쪽 아래로 내려가는 대각선
        if i % 3 == 1:
            while True:
                arr[j][k] = num
                num += 1
                j += 1
                if j >= n or arr[j][k]:
                    j -= 1
                    k += 1
                    break
        # 왼쪽에서 오른쪽 향하는 일직선
        elif i % 3 == 2:
            while True:
                arr[j][k] = num
                num += 1
                k += 1
                if k >= n or arr[j][k]:
                    k -= 2
                    j -= 1
                    break
        # 왼쪽 위로 향하는 대각선
        elif i % 3 == 0:
            while True:
                arr[j][k] = num
                num += 1
                j -= 1
                k -= 1
                if arr[j][k]:
                    j += 2
                    k += 1
                    break

    return sum(arr, [])