# 구현 - 이항 계수1
# Solution 
# (1) 그냥 내장 함수 쓰기 import math -> o
import math

n, k = map(int, input().split())
print(math.factorial(n)//math.factorial(n-k)//math.factorial(k))