T = int(input())
for test_case in range(1, T+1):
    a, b = 1, 1
    v = list(input())
    for i in range(len(v)):
        if v[i] == 'L':
            b = a+b
        else:
            a = a+b

    print('#{} {} {}'.format(test_case, a, b))
