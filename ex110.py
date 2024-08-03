a = set(map(int, input().split()))
b = set(map(int, input().split()))

s = a - b

print(*sorted(s))

# 8 5 3 5 -3 1
# 1 2 3 4