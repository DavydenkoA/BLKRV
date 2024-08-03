n = int(input())
a = [x for x in range(1, n+1) if n % x == 0]
print(*a)

# 10