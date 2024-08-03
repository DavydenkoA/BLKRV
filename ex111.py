a = set(map(int, input().split()))
b = set(map(int, input().split()))

s = a ^ b

print(*sorted(s))

# 1 2 3 4 5
# 4 5 6 7 8