p = 1
x = 1
while x != 0:
    x = int(input())
    if x > 0:
        p *= x
    else:
        continue
print(p)