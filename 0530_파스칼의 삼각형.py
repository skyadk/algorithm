#크기가 N인 파스칼의 삼각형을 만들어야 한다.
# 파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
# 1. 첫 번째 줄은 항상 숫자 1이다.
# 2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
# N이 4일 경우,
# N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    lst = [1] * 10
    print('#{}'.format(test_case))
    if n == 1:
        print(*lst[:1])
    elif n == 2:
        print(*lst[:1])
        print(*lst[:2])
    else:
        print(*lst[:1])
        print(*lst[:2])
        for j in range(3, n+1):
            tmp = lst[:]
            for i in range(j-2):
                tmp[i+1] = lst[i] + lst[i+1]
            lst = tmp[:]
            print(*lst[:j])

    # print('#{} {}'.form                                        at(test_case, result))
