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

    