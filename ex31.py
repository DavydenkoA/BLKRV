n = int(input())
vklad = [1000]
count = 0
while count < n:
    b = vklad[-1] * 1.05
    vklad.append(b)
    count += 1
print(round(vklad[-1], 2))