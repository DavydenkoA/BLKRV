digs = tuple(map(int, input().split()))
a = ()
for x in digs:
    if x in a:
        continue
    else:
        a = a + (x,)

print(*a)




# 8 11 -5 -2 8 11 -5 9 3 9 4 7 12