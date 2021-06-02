dx = [-1,-1, 0, 1, 1, 1, 0,-1]
dy = [ 0, 1, 1, 1, 0,-1,-1,-1]


def check5(x, y, n, arr):
    for i in range(8):
        cnt = 1

        for k in range(1, 6):
            nx = x+dx[i]*k
            ny = y+dy[i]*k
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                break
            if arr[nx][ny] != 'o':
                break

            cnt = cnt + 1

        if cnt >= 5:
            return True

    return False

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    game_over = False
    for i in range(n):
        for j in range(n):
            if game_over:
                break
            if arr[i][j] == 'o':
                game_over = check5(i, j, n, arr)

    if game_over:
        print('#{} YES'.format(test_case))
    else:
        print('#{} NO'.format(test_case))




