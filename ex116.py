s = input().split()
x = int(s.pop(0))
a = {x: s[0] for x, s[0] in zip(range(int(x),len(s)+1),s)}
print(a.get(4))


# 1 ужасно неудовлетворительно удовлетворительно прилично отлично