
def dfs(current, n):
    global visited, check
    print(current, end=' ')
    visited[current] = True ##방문체크
    for i in range(1, n+1):
        if check[current][i] == 1:
            if not visited[i]:
                dfs(i, n)


def bfs(current, n):
    global visited2, check
    queue = []
    queue.append(current)
    visited2[current] = True
    while len(queue) != 0 :
        tmp = queue.pop(0)
        print(tmp, end=' ')
        for i in range(1, n + 1):
            if check[tmp][i] == 1 and visited2[i] == False:
                visited2[i] = True
                queue.append(i)


N, M, V = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]

check = [[0]*(N+1) for i in range(N+1)]

visited = [False for i in range(N+1)]
visited2 = [False for i in range(N+1)]

for i in range(M):
    check[arr[i][0]][arr[i][1]] = 1
    check[arr[i][1]][arr[i][0]] = 1

dfs(V,N)
print()
bfs(V,N)
