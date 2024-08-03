a = set(input().split())
b = set(input().split())
s = a & b

print(*sorted(s))

# 8 11 12 15 -2
# 4 11 10 15 -5 1 -2
