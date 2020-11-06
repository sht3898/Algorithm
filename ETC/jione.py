from collections import deque

n,m = map(int,input().split())      # 행,열 개수 입력 받음

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))        #행,열 크기에 맞게 0과 1로만 된 2차원 리스트 입력

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))     #큐에 (x,y)를 넣음

    while queue:            #큐가 비어있지않은 동안
        x, y = queue.popleft()      #큐에서 맨 끝에 요소를 빼 x,y로 저장

        for i in range(4):
            nx = x + dx[i]      #현재 위치에서 우측 한칸 아래 한칸을 검사
            ny = y + dy[i]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:    #영역을 벗어나면 무시
                continue

            if graph[nx][ny] == 0:      #0이면 무시
                continue

            if graph[nx][ny] == 1:      #해당 위치가이 1이면(처음 방문이면)
                graph[nx][ny] = graph[x][y]+1     #전 위치에서 +1하여 현재 칸에 저장
                queue.append((nx, ny))      # 현재칸을 큐에 넣음


for i in range(n):
    for j in range(m):      #영역 전체에 bfs를 수행
        bfs(i,j)
maxsize = max(map(max,graph))       #graph에서 가장 큰 수가 가장 큰 영역의 크기이므로 maxsize로 저장 (2차원 리스트라 max 두번)



print(maxsize)