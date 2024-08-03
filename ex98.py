names = tuple(map(str, input().lower().split()))
lst = []
for x in names:
    if 'ва' in x:
        lst.append(x)

print(*lst)


# Петя Варвара Венера Василиса Василий Федор