def dfs(N, cnt, l):
    global visited
    if cnt == N:
        ans.append(l)
        return
    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        dfs(N, cnt+1, l+[lst[i]])
        visited[i] = 0


N = int(input())
lst = list(map(int, input().split()))
visited = [0] * len(lst)
ans = []
l = []
cnt = 0

dfs(N, cnt, l)
print(ans)