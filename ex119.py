s = input().lower().split()

m = {x: s.count(x) for x in s}

print(m.get('и', 0))

# И что сказать и что сказать и нечего и точка