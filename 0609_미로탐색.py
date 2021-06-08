from collections import deque

def bfs(arr, visited):
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for nx,ny in [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]:
            if not (0 <= nx < N) or not(0 <= ny < M):
                continue
            if arr[nx][ny] == 0:
                continue
            if visited[nx][ny] >= 0:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx,ny])


N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

bfs(arr,visited)
print(*visited, sep="\n")