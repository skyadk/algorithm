# D L N


T = int(input())
for test_case in range(1, T+1):
    rst = 0
    D, L, N = map(int, input().split())
    for i in range(0, N):
        rst = rst + D * (1 + i*L/100)
    print('#{} {}'.format(test_case, int(rst)))