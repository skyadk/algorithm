

score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    total_arr = []
    for i in range(n):
        mid, fin, rep = map(int, input().split())
        total = mid*0.35 + fin*0.45 + rep*0.2
        total_arr.append(total)
    kscore = total_arr[k-1]
    print(kscore)
    print(total_arr)
    total_arr.sort(reverse=True)
    print(total_arr)
    idx = total_arr.index(kscore) // (n//10) # 10 // 3 = 3  , round는 반올림
    print('#{} {}'.format(test_case, score[idx]))