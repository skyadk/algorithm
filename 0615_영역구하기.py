from collections import deque


def bfs(arr, visited,ans,i,j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    result = 1
    while q:
        x, y = q.popleft()
        for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if not (0 <= nx < N) or not (0 <= ny < M):
                continue
            if arr[nx][ny] == 1:
                continue
            if visited[nx][ny] == 1:
                continue
            visited[nx][ny] = 1
            result = result + 1
            q.append([nx, ny])
    ans.append(result)


M, N, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = []
ans = []
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1
visited = arr

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            bfs(arr, visited, ans,i,j)

ans.sort()
print(len(ans))
print(*ans)

