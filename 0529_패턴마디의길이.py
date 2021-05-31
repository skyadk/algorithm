#//패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = ''
    string = input()
    for pattern_len in range(1, len(string)):
        if string[:pattern_len] == string[pattern_len:pattern_len+pattern_len]:
            result = pattern_len
            break
        else:
            continue

    print('#{} {}'.format(test_case, result))

