import sys

sys.setrecursionlimit(10**6)

def dfs(target,l,cnt, n):
    global chk
    if cnt == n and l > target and chk == 0:
        ans.append(l)
        chk = 1
        return
    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        dfs(target, l+[lst[i]], cnt+1, n)
        if chk:
            break
        visited[i] = 0


N = int(input())
lst = list(map(int, input().split()))
target = lst[:]
lst.sort()
visited = [0] * N
ans = []
chk = 0
dfs(target, [], 0, N)
if ans:
    print(*ans[0])
else:
    print(-1)
