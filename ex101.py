N = int(input())
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))

cnt = 0
for i, d in enumerate(t):
    if cnt < N:
        print(*d[:N])
        #print(*d[:N])
    cnt += 1


# for i in c:
#     print(*i)
# 3