# Level3

## [섬 연결하기](https://programmers.co.kr/learn/courses/30/lessons/42861)

* 풀이

  * 비용을 오름차순으로 정렬하여 최소 비용이 먼저 오게함
* costs의 첫번째 원소를 routes에 넣어서 첫 경로로 설정
  
  * 모든 섬이 경로에 들어올때까지(`len(routes) == n`) 원소들을 반복하면서 경로를 탐색
* 만약 시작점과 도착점이 이미 경로에 있다면 넘어감
  * 둘중 한점만 경로에 있다면 새로운 섬을 경로에 추가하고(set자료형이기 때문에 중복된 섬은 추가되지 않음) ans에 현재 섬의 비용을 추가한다. 또한, 현재 섬의 경로를 [-1, -1, -1]로 설정하여 다음 반복에 사용되지 않게 함

  

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

* 기타
  * 탐욕법을 이용하여 네트워크 정점을 최소비용으로 연결
    * 탐욕법이란 그때그때 최선의 선택을 함으로써 최선의 결과에 도달하는 것
    * 사이클이 생성되지 않게하는 것이 핵심
* [참고링크](https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level3-%EC%84%AC-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0-%ED%83%90%EC%9A%95%EB%B2%95)
* [크루스칼 알고리즘](https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html)



## [네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)

* 풀이1(BFS)

  * collections 라이브러리에서 deque를 불러옴
* 방문했던 컴퓨터를 저장하기 위한 visit 선언
  
  * 함수를 만든 뒤 큐를 이용한 bfs 탐색으로 현재 컴퓨터에서 갈 수 있는 모든 지점을 탐색하며 visit 체크
* 반복문을 통해 아직 방문하지 않은 컴퓨터에서 갈 수 있는 모든 지점을 체크하며 answer에 1 추가
  
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

  * 방문했던 컴퓨터를 저장하기 위한 visit 선언
* 함수를 만든 뒤 재귀를 통해 방문하지 않은 컴퓨터를 모두 수환하며 visit 체크
  
* 반복문을 통해 아직 방문하지 않은 컴퓨터에서 갈 수 있는 모든 지점을 체크하며 answer에 1 추가
  
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

  

## [여행경로](https://programmers.co.kr/learn/courses/30/lessons/43164)

* 풀이

  * dict 자료형인 routes를 통해 시작지에서 갈수 있는 여행지들을 추가하고 각 시작지 별로 갈 수 있는 여행지들을 알파벳 순서대로 정렬함
* 시작점은 저장할 stack과 경로를 저장할 path를 선언
  
  * 시작점이 routes에 없거나 모든 곳을 다 방문한 경우 시작점(top)을 path에 저장
* 그것이 아니라면 현재 시작점에서 갈 수 있는 여행지 중 알파벳 순서가 가장 빠른 여행지를 시작점 스택에 추가
  
* 반복문이 끝나면 도착지점부터 저장했으므로 경로를 거꾸로 반환하며 끝냄
  
* 코드

  ```python
  def solution(tickets):
      routes = {}
      for t in tickets:
          if t[0] not in routes:
              routes[t[0]] = [t[1]]
          else:
              routes[t[0]].append(t[1])
              routes[t[0]].sort()
  
      stack = ['ICN']
      path = []
      while stack:
          top = stack[-1]
          if top not in routes or len(routes[top]) == 0:
              path.append(stack.pop())
          else:
              stack.append(routes[top].pop(0))
  
      return path[::-1]
  ```

  

* 기타

  ```python
  def solution(tickets):
      answer = []
      routes = []
      tickets.sort()
      for i, icn in enumerate(tickets):
          if icn[0] == 'ICN':
              routes.append(tickets.pop(i))
              break
      while tickets:
          for i, city in enumerate(tickets):
              if routes[-1][1] == city[0]:
                  routes.append(tickets.pop(i))
                  break
      answer = list(map(lambda x:x[0], routes))
      answer.append(routes[-1][1])
      return answer
  ```

  * 처음엔 위와 같은 방식으로 풀었으나

    ```python
    ticket
    1. "ICN" -> "AAA"
    2. "ICN" -> "BBB"
    3. "BBB" -> "ICN"
    ```

    이런 상황에서 오류가 발생하기 때문에 수정이 필요했음

* [참고링크](https://programmers.co.kr/learn/courses/30/lessons/43164)



## [감시카메라](https://programmers.co.kr/learn/courses/30/lessons/42884)

* 풀이1

  * 진출 기점을 기준으로 오름차순 정렬
  * 최대 -30000이므로 초기 카메라 위치를 -30001로 설정
  * `routes` 배열을 반복하면서 카메라가 진입 지점(`route[0]`)보다 작은지 확인
  * 작다면, 현재 카메라 위치로 해당 차량을 만나지 못했다는 의미이므로 카메라를 추가로 세우고, 가장 최근 카메라의 위치(`route[1]`)를 갱신

* 코드1

  ```python
  def solution(routes):
      answer = 0
      routes.sort(key=lambda x: x[1])
      camera = -30001
  
      for route in routes:
          if camera < route[0]:
              answer += 1
              camera = route[1]
      return answer
  ```

* 풀이2

  * 카메라를 만났는지에 대한 check 배열을 만들고 각 구간을 모두 검사
  * 이중 for문을 사용하면서 시간복잡도가 O(n^2)가 걸림으로 풀이1에 비해 효율이 좋지 않음

* 코드2

  ```python
  def solution(routes):
      answer = 0
      routes.sort(key=lambda x: x[1])
      leng = len(routes)
      checked = [0] * leng
  
      for i in range(leng):
          if checked[i] == 0:
              camera = routes[i][1]
              answer += 1
          for j in range(i + 1, leng):
              if routes[j][0] <= camera <= routes[j][1] and checked[j] == 0:
                  checked[j] = 1
      return answer
  ```

* [참고링크](https://wwlee94.github.io/category/algorithm/greedy/speed-enforcement-camera/)



## [베스트앨범](https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3)

* 풀이

  ```python
  def solution(genres, plays):
      answer = []
      music = {}
      music_cnt = {}
      for i in range(len(genres)):
          if genres[i] not in music:
              music[genres[i]] = [[i, plays[i]]]
              music_cnt[genres[i]] = plays[i]
          else:
              music[genres[i]].append([i, plays[i]])
              music_cnt[genres[i]] += plays[i]
  
      for k, v in music.items():
          v.sort(key=lambda x: (-x[1], x[0]))
      music_cnt = sorted(music_cnt.items(), key=lambda x: -x[1])
  
      for key, value in music_cnt:
          if len(music[key]) >= 2:
              answer.extend(list(map(lambda x: x[0], music[key][:2])))
          else:
              answer.append(music[key][0][0])
      return answer
  ```

  * 장르별로 음악의 정보를 담을 딕셔너리 music과 장르별 재생 수를 담을 딕셔너러 music_cnt 선언
  * 장르와 재생 수 리스트의 길이만큼 반복하면서 music과 music_cnt에 정보 저장
  * music에 저장된 장르별 정보를 재생수 기준 내림차순 와 인덱스 기준 오름차순으로 정렬
  * music_cnt를 장르별 재생수 내림차순 정보가 저장된 리스트 자료형으로 바꿔서 저장
  * 장르에 포함된 노래가 2곡 이상인 장르는 answer에 상위 두 개의 데이터만 저장하고, 한 곡만 있는 장르는 한개만 저장

* 매직코드를 사용한 다른 풀이

  ```python
  def solution(genres, plays):
      answer = []
      dic = {}
      album_list = []
      for i in range(len(genres)):
          dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
          album_list.append(album(genres[i], plays[i], i))
  
      dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
      album_list = sorted(album_list, reverse=True)
  
      print(album_list)
  
      while len(dic) > 0:
          play_genre = dic.pop(0)
          print(play_genre)
          cnt = 0;
          for ab in album_list:
              if play_genre[0] == ab.genre:
                  answer.append(ab.track)
                  cnt += 1
              if cnt == 2:
                  break
  
      return answer
  
  class album:
      def __init__(self, genre, play, track):
          self.genre = genre
          self.play = play
          self.track = track
  
      def __lt__(self, other):
          return self.play < other.play
      def __le__(self, other):
          return self.play <= other.play
      def __gt__(self, other):
          return self.play > other.play
      def __ge__(self, other):
          return self.play >= other.play
      def __eq__(self, other):
          return self.play == other.play
      def __ne__(self, other):
          return self.play != other.play
  ```

  * 아직 매직코드는 익숙하지 않은데 공부를 더 하면 좋을 것 같다

