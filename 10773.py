# 구현 - 제로
# Solution
# (1) 전형적 if문
n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    if num==0:
        arr.pop()
    else:
        arr.append(num)

print(sum(arr))