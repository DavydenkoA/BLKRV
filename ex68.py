n = int(input())
k = [64, 32, 16, 8, 4, 2, 1]
r = []
if n == 0:
    print(0)
for i in range(len(k)):
    while n >= k[i]:
        n = n - k[i]
        r.append(k[i])
        if k[i] > n:
            continue
print(*r)


# 221