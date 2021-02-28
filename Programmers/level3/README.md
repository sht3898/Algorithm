# Level3

## [섬 연결하기](https://programmers.co.kr/learn/courses/30/lessons/42861)

* 풀이

  ```python
  def solution(n, costs):
      # kruskal algorithm
      ans = 0
      costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
      routes = set([costs[0][0]]) # 집합
      while len(routes)!=n:
          for i, cost in enumerate(costs):
              if cost[0] in routes and cost[1] in routes:
                  continue
              if cost[0] in routes or cost[1] in routes:
                  routes.update([cost[0], cost[1]])
                  ans += cost[2]
                  costs[i] = [-1, -1, -1]
                  break
      return ans
  ```



* [크루스칼 알고리즘(Kruskal Algorithm) 활용](https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level3-%EC%84%AC-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0-%ED%83%90%EC%9A%95%EB%B2%95)

  * 탐욕법을 이용하여 네트워크 정점을 최소비용으로 연결
  * 탐욕법이란 그때그때 최선의 선택을 함으로써 최선의 결과에 도달하는 것
  * 사이클이 생성되지 않게하는 것이 핵심

  