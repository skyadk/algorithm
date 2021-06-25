from collections import deque

def bfs(arr, visited):
    q = deque()
    q.append([0, 0, 1])
    visited[1][0][0] = 1
    while q:
        x, y, dig = q.popleft()
        if x == N-1 and y == M-1:
             return visited[dig][N-1][M-1]
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            ndig = dig
            if not(0 <= nx < N and 0 <= ny < M):
                continue
            if visited[ndig][nx][ny] > 0:
                continue
            if arr[nx][ny] == 1:
                if ndig == 0:
                    continue
                if ndig == 1:
                    ndig = 0

            visited[ndig][nx][ny] = visited[dig][x][y] + 1
            q.append([nx, ny, ndig])
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[-1]*M for _ in range(N)] for _ in range(2)]
print(bfs(arr, visited))
# print(*visited[0], sep='\n')
# print()
# print(*visited[1], sep='\n')