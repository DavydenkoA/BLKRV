a = int(input())
b = [1, 1]
d = 0
while d < a:
    c = b[-1] + b[-2]
    b.append(c)
    d = len(b)
print(*b)


# 8