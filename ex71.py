N = int(input())
c = [[1 if j==i else 0 for i in range(N)]for j in range(N)]

for i in c:
    print(*i)
# 4