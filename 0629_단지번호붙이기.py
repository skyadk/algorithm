from collections import deque


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if not (0 <= nx < N and 0 <= ny <N):
                continue
            if visited[nx][ny] == 0:
                continue
            visited[nx][ny] = 0
            cnt += 1
            q.append([nx, ny])
    return cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = arr
lst = []
house_cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            house_cnt += 1
            lst.append(bfs(i, j))

lst.sort()
print(house_cnt)
print(*lst, sep='\n')