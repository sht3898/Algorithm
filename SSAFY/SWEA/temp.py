def MyCalc(y):
    global sub_result, result

    if sub_result <= result:
        return

    if y == N:
        result = sub_result
        return

    for x in range(N):
        if not visited[x]:
            if Table[y][x] == 0:
                continue
            else:
                sub_result *= (Table[y][x]/100)
                visited[x] = True
                MyCalc(y+1)
                sub_result /= (Table[y][x]/100)
                visited[x] = False


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Table = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sub_result, result = 1, 0
    MyCalc(0)
    print('#%d %0.6f'%(tc, round(result*100, 6)))