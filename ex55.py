digs = list(map(str, input().split()))
double = ' '
for i, d in enumerate(digs):
    double += d + ' ' + d + ' '

print(double)

# 8 11 2