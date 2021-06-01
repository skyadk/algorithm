
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    for i in range(9, 0, -1):
        if n % i == 0:
            if n / i >= 10:
                print('#{} No'.format(test_case))
                break
            else:
                print('#{} Yes'.format(test_case))
                break
        else:
            continue



    # print('#{}'.format(test_case))

