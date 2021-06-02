T = int(input())
for test_case in range(1, T+1):
    rst = 0
    #N을 입력받자
    N = int(input())
    v = list(map(int, input().split()))
    for i in range(N-2):
        key = v[i+1]
        s = sorted(v[i:i+3])
        if key == s[1]:
            rst = rst + 1

    print('#{} {}'.format(test_case, rst))


#split() = split(' ')   ['hello','world']
#split('') z 원소단위    ['h','e','l',' ',]