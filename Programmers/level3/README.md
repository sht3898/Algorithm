# Level3

# [섬 연결하기](https://programmers.co.kr/learn/courses/30/lessons/42861)

* 풀이

  비용을 오름차순으로 정렬하여 최소 비용이 먼저 오게함

  costs의 첫번째 원소를 routes에 넣어서 첫 경로로 설정

  모든 섬이 경로에 들어올때까지(`len(routes) == n`) 원소들을 반복하면서 경로를 탐색

  만약 시작점과 도착점이 이미 경로에 있다면 넘어감

  둘중 한점만 경로에 있다면 새로운 섬을 경로에 추가하고(set자료형이기 때문에 중복된 섬은 추가되지 않음) ans에 현재 섬의 비용을 추가한다. 또한, 현재 섬의 경로를 [-1, -1, -1]로 설정하여 다음 반복에 사용되지 않게 함

  

* 코드

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
  
* [크루스칼 알고리즘](https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html)



# [네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)

* 풀이1(BFS)

  collections 라이브러리에서 deque를 불러옴

  방문했던 컴퓨터를 저장하기 위한 visit 선언

  함수를 만든 뒤 큐를 이용한 bfs 탐색으로 현재 컴퓨터에서 갈 수 있는 모든 지점을 탐색하며 visit 체크

  반복문을 통해 아직 방문하지 않은 컴퓨터에서 갈 수 있는 모든 지점을 체크하며 answer에 1 추가

* 코드1(BFS)

  ```python
  from collections import deque
  
  
  def solution_bfs(n, computers):
      answer = 0
      visit = [0] * n
  
      def bfs(x):
          Q = deque()
          Q.append(x)
          visit[x] = 1
          while Q:
              x = Q.popleft()
              for j in range(n):
                  if x != j and computers[x][j]:
                      if not visit[j]:
                          Q.append(j)
                          visit[j] = 1
      for i in range(n):
          if not visit[i]:
              bfs(i)
              answer += 1
      return answer
  ```

  

* 풀이2(DFS)

  방문했던 컴퓨터를 저장하기 위한 visit 선언

  함수를 만든 뒤 재귀를 통해 방문하지 않은 컴퓨터를 모두 수환하며 visit 체크

  반복문을 통해 아직 방문하지 않은 컴퓨터에서 갈 수 있는 모든 지점을 체크하며 answer에 1 추가

* 코드2(DFS)

  ```python
  def solution_dfs(n, computers):
      answer = 0
      visit = [0] * n
  
      def dfs(x):
          visit[x] = 1
          for j in range(n):
              if x != j and computers[x][j]:
                  if not visit[j]:
                      dfs(j)
  
      for i in range(n):
          if not visit[i]:
              dfs(i)
              answer += 1
      return answer
  ```

  

