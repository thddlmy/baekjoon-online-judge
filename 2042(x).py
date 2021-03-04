# 구간 합 - 결과 X -> 시간 초과, 세그먼트 트리로 해결?

def modify_prefix(arr, p, b, c):
    arr[b-1] = c
    del p[1:len(p)]
    get_prefix(arr, p)

def get_prefix(arr, p):
    sum = 0
    for i in arr:
        sum += i
        p.append(sum)

N, M, K = map(int, input().split())
p = [0]
arr = []
result = []

# 숫자 입력
for i in range(N):
    num = int(input())
    arr.append(num)

# a=1 or a=2인 상황
for i in range(M+K):
    a, b, c = map(int, input().split())
    if a==1:
        modify_prefix(arr, p, b, c)
    else:
        result.append(p[c]-p[b-1])

for i in result:
    print(i)