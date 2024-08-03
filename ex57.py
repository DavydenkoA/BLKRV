digs = list(map(float, input().split()))

for i, d in enumerate(digs):
    if d < 0:
        digs[i] = -1.0
    else:
        continue

print(*digs)

# -5.67 3.5 6.89 -3.0