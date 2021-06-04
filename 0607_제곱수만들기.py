T = int(input())
for test_case in range(1, T+1):
    A = int(input())
    insu = []
    i=2
    rst = 1
    pre = 0

    while A != 1:
        if A % i == 0:
            A = A // i
            insu.append(i)
        else:
            i += 1

    for k in range(len(insu)):
        if pre == insu[k]:
            continue
        if insu.count(insu[k]) % 2 == 1:
            pre = insu[k]
            rst = rst * insu[k]

    print('#{} {}'.format(test_case, rst))