T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str = input()
    charList = list(str)
    charList.sort()
    if charList[0] == charList[1] and charList[2] == charList[3]:
        if charList[1] == charList[2]:
            print('#{} No'.format(test_case))

        else:
            print('#{} Yes'.format(test_case))

    else:
        print('#{} No'.format(test_case))



