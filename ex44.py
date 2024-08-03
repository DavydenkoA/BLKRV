s = []
for x in range(-2, -11, -2):
    s.append(x)
    x += 1
s.reverse()
print(*s)