n = int(input())
x = []
i = 1
while i <= n:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        x.append(i)
    if n >= 100:
        print("слишком большое значение n")
        break
else:
    print(*x)