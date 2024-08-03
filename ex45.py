a = list(map(int, input().split()))
s = 0
for i in range(len(a)):
    if a[i] % 2 == 1:
        s += a[i]
print(s)

# 8 11 -2 4 0 13 19 12 7

# s += i на s += a[i]