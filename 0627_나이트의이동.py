from collections import deque


def bfs():
    global M, sx, sy, ex, ey
    q = deque()
    q.append([sx, sy])

    visited = [[0] * M for _ in range(M)]

    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return print(visited[x][y])

        for nx, ny in [(x - 2, y + 1), (x - 1, y + 2), (x + 1, y + 2), (x + 2, y + 1), (x + 2, y - 1), (x + 1, y - 2),
                       (x - 1, y - 2), (x - 2, y - 1)]:
            if not (0 <= nx < M and 0 <= ny < M):
                continue
            if visited[nx][ny] > 0:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny])

test_case = int(input())

for _ in range(test_case):
    M = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    bfs()
