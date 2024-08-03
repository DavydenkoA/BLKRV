a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = len(a)
L = [(a[i] + b[i]) for i in range(n)]
print(*L)
# 1 2 3 4 5
# 6 7 8 9 10