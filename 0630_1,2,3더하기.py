def dfs(n, sum):
    global arr, rst
    if sum > n:
        return
    if sum == n:
        rst += 1
    for index in range(3):
        dfs(n, sum+arr[index])


arr = [1, 2, 3]
test_case = int(input())
rst = 0
s = 0
for _ in range(test_case):
    num = int(input())
    dfs(num, s)
    print(rst)
    rst = 0
