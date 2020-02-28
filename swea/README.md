# SWEA

## [1952_수영장](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq)

* 풀이

  ```python
  def solve(k, s):
      global MIN
      if k >= 13:
          MIN = min(MIN, s)
      else:
          solve(k+1, s+fees[0]*plans[k])
          solve(k+1, s+fees[1])
          solve(k+3, s+fees[2])
  
  
  for TC in range(1, int(input())+1):
      fees = list(map(int, input().split()))
      plans = [0] + list(map(int, input().split()))
      MIN = fees[3]
      solve(1, 0)
      print('#{} {}'.format(TC, MIN))
  
  ```

  

## [4008_숫자만들기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH)

* 풀이

  ```python
  def solve(k, plus, minus, multiple, divide, s):
      global MAX, MIN
      if k == N:
          MAX = max(MAX, s)
          MIN = min(MIN, s)
      else:
          if plus:
              solve(k+1, plus-1, minus, multiple, divide, s+numbers[k])
          if minus:
              solve(k+1, plus, minus-1, multiple, divide, s-numbers[k])
          if multiple:
              solve(k+1, plus, minus, multiple-1, divide, s*numbers[k])
          if divide:
              if s >= 0:
                  solve(k+1, plus, minus, multiple, divide-1, s // numbers[k])
              elif s < 0:
                  solve(k+1, plus, minus, multiple, divide-1, -(-s // numbers[k]))
  
  
  for TC in range(1, int(input())+1):
      N = int(input())
      arr = list(map(int, input().split()))   # +, -, *, / 개수
      numbers = list(map(int, input().split()))   # 주어진 숫자
      MAX = -1e9
      MIN = 1e9
      solve(1, arr[0], arr[1], arr[2], arr[3], numbers[0])
      print('#{} {}'.format(TC, MAX - MIN))
  
  ```

* solve 할 때, solve(0, arr[0], arr[1], arr[2], arr[3], 0)로 하면 안 되는 이유가 궁금