def solution(sizeOfMatrix, matrix):
    cnt = 0
    area = []
    visit = [[0] * sizeOfMatrix for _ in range(sizeOfMatrix)]
    Q = []
    for i in range(sizeOfMatrix):
        for j in range(sizeOfMatrix):
            if not visit[i][j] and matrix[i][j]:
                cnt += 1
                area_cnt = 0
                Q.append((i, j))
                while Q:
                    x, y = Q.pop()
                    visit[x][y] = 1
                    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < sizeOfMatrix and 0 <= ny < sizeOfMatrix and not visit[nx][ny] and matrix[nx][ny]:
                            Q.append((nx, ny))
                            visit[nx][ny] = 1
                            area_cnt += 1
                area.append(area_cnt+1)
    area.sort()
    print(cnt)
    print(*area)


if __name__ == '__main__':
    # sizeOfMatrix = int(input())
    # matrix = [list(map(int, input().split())) for _ in range(sizeOfMatrix)]
    sizeOfMatrix = 6
    matrix = [[0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 1, 0], [1, 1, 1, 0, 0, 0]]
    solution(sizeOfMatrix, matrix)
