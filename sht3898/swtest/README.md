# SW Test 대비

## 14888_연산자끼워넣기

[링크](https://www.acmicpc.net/problem/14888)

* 풀이

  * [N과 M 문제](https://www.acmicpc.net/workbook/view/2052)의 응용 버젼

  * solve 함수에서 연산자를 인자로 넘겨서 풀이

  * 음수를 //로 나눌 경우 원래 값의 절대값 보다 1이 적은 수가 나옴

  * 이를 방지하기 위해 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼다

  * 전체 코드

    ```python
    def solve(k, result, plus, minus, multiple, divide):
        global MAX, MIN
        if k == N:
            MAX = max(result, MAX)
            MIN = min(result, MIN)
            return
        if plus:
            solve(k+1, result + numbers[k], plus-1, minus, multiple, divide)
        if minus:
            solve(k+1, result - numbers[k], plus, minus-1, multiple, divide)
        if multiple:
            solve(k+1, result * numbers[k], plus, minus, multiple-1, divide)
        if divide:
            if result >= 0:
                solve(k+1, result//numbers[k], plus, minus, multiple, divide-1)
            elif result < 0:
                solve(k+1, -(-result//numbers[k]), plus, minus, multiple, divide-1)
        return
    
    
    
    N = int(input())
    numbers = list(map(int, input().split()))
    operator = list(map(int, input().split()))
    MAX, MIN = -1e9, 1e9
    solve(1, numbers[0], operator[0], operator[1], operator[2], operator[3])
    print(MAX, MIN)
    
    ```


## 11399_atm

[링크](https://www.acmicpc.net/problem/11399)

* 풀이

  * 대기 시간이 계속 늘어나므로 대기 시간을 저장할 변수 필요 => waiting_times

  * 전체 시간을 계산할 변수 필요 => total_times

  * 정렬을 해야 시간이 최소가 됨 => sorted

  * 전체코드

    ```python
    def solve(times):
        total_time = 0
        waiting_time = 0
        times.sort()
        for time in times:
            waiting_time += time
            total_time += waiting_time
        return total_time
    
    
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    print(solve(arr))
    
    ```



## 11047_동전0

[링크](https://www.acmicpc.net/problem/11047)

* 풀이

  * 동전의 최소 개수를 찾아야하므로 큰 수부터 찾는 것이 좋음

  * while 반복문을 통해 조건이 맞을 동안 반복

  * 저장된 값에 새 값을 더한 것이 목표값보다 크다면 작은 숫자로 바꾸고, 작다면 새 값을 더하고 cnt에 1을 더한다.

  * 전체 코드

    ```python
    N, K = map(int, input().split())
    arr = sorted([int(input()) for _ in range(N)], reverse=True)
    idx = 0
    tmp = 0
    cnt = 0
    while tmp != K:
        if tmp + arr[idx] > K:
            idx += 1
        elif tmp + arr[idx] <= K:
            tmp += arr[idx]
            cnt += 1
    print(cnt)
    
    ```

    