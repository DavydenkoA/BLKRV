n = int(input())
s = 0
for x in range(n):
    if x % 3 == 0 or x % 5 == 0:
        s += x
print(s)

#print(n)


