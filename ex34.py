p = [0] * 10
i = 0

while sum(p) < 5:
    i = int(input())
    if p[i] == 1:
        continue
    p[i] = 1
print(" ".join(map(str, p)))

