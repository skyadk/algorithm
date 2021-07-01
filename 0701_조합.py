def dfs(n, r, dep, cnt, l):
    if cnt == r:
        ans.append(l)
        return
    for i in range(dep,N):
        if visited[i] == 1:
            return
        visited[i] = 1
        dfs(n, r, i+1, cnt+1, l+[lst[i]])
        visited[i] = 0


N = int(input())
lst = list(map(int, input().split()))
visited = [0] * N
ans = []
l = []
dfs(N, 3, 0, 0, l)
print(ans)