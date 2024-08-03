digs = list(map(float, input().split()))
number = digs[0]
for i in digs:
    if number > i:
        number = i
    else:
        continue

print(number)

# 8.6 9.11 -4.567 -10.0 1.45