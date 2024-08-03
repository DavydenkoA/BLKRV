digs = tuple(map(int, input().split()))

for i, d in enumerate(digs):
    if digs.count(d) > 1:
        print(i, end = ' ')

#print(a)

# 5 4 -3 2 4 5 10 11