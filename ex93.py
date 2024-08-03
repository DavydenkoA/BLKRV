import sys

# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']

# здесь продолжайте программу (используйте список lst_in)
d = {}

for x in lst_in:
    #bd, name = x.split()[0:2], x.split()[2:]
    bd, name = x.split()
    if bd in d.keys():
        d[bd].append(name)
    else:
        d[bd] = [name]
for g in d:
    print(f'{g[0:2]}: {", ".join(d[g[0:2]])}')
# for x in lst_in:
#     if x[0:2] in d.keys():
#         d[x[0:2]].append(x[2:])
#     else:
#         d[x[0:2]] = [x[2:]]
# for g in d:
#     print(f'{g.split()[0:2]}: {", ".join(d[g[0:2]])}')



# for i in lst_in:
#     bd, *name = i.split()...



# for x in lst_in:
#     if x[0] in d.keys():
#         print(d[x[0]])
#
#         d[x[0]].append(x[2:])
#     else:
#         a = d.fromkeys(x[0], x[2:])
#         d.update(a)

#print(*sorted(d.items()))
