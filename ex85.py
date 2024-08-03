d = dict([x.split('=') for x in input().split()])
if "False" in d:
    del d['False']
if "3" in d:
    del d['3']
#print(d)
print(*sorted(d.items()))

# лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина