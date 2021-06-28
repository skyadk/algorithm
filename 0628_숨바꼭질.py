from collections import deque


def bfs(x, k):
    q = deque()
    q.append(x)
    visited = [-1] * 100001
    visited[x] = 0

    while q:
        x = q.popleft()
        if x == k:
            return print(visited[x])

        for nx in [x - 1, x+1, x*2]:
            if not (0 <= nx < 100001):
                continue
            if visited[nx] >= 0:
                continue
            visited[nx] = visited[x] + 1
            q.append(nx)


N, K = map(int, input().split())

bfs(N, K)
