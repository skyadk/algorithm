from collections import deque


def bfs():
    global flag
    q = deque()
    result = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if visited[k][i][j] == 1:
                    q.append([k, i, j, result])
    if not q: #처음다돌았는데 다 0 또는 -1이다(안익었거나, 빈공간이다. >> 번져나갈수없다.)
        flag = 0
    while q:
        z, x, y, result = q.popleft()
        for nz, nx, ny in [(z, x - 1, y), (z, x, y + 1), (z, x + 1, y), (z, x, y - 1), (z - 1, x, y), (z + 1, x, y)]:
            # print(nz,nx,ny)
            if not (0 <= nz < H and 0 <= nx < N and 0 <= ny < M):
                continue
            if visited[nz][nx][ny] == 1 or visited[nz][nx][ny] == -1:
                continue
            if arr[nz][nx][ny] == -1:
                continue
            visited[nz][nx][ny] = 1
            q.append([nz, nx, ny, result + 1])
    #print(*visited, sep='\n')
    return result

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = arr
flag = 1

res = bfs()

for k in range(H):
    for i in range(N):
        for j in range(M):
            if visited[k][i][j] == 0: #다돌렸는데 0 남아있따. >> 더 불가능하다 >>-1출력
                flag = -1
                break

if flag == 1:
    print(res)  # result =0 >> 다익었따. 0출력
elif flag == -1: #-1
    print(flag)
elif flag == 0:
    print(-1)

