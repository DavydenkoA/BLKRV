n, m = map(int, input().split())
lst = [n, m]
while lst[-2] < lst[-1]:
    b = lst[-2] + 1
    lst.insert(-1, b)
lst.remove(m)
print(*lst[1::2])



# 2 10