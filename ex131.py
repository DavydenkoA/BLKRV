def get_odd(x):
    if x % 2 != 0:
        return True
    else:
        return False


a = list(map(int, input().split()))
lst = []
for i in a:
    if get_odd(i):
        lst.append(i)

print(*lst)

# 8 11 -15 3 2 10