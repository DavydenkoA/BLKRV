import sys
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

d = {}
for s in lst_in:
    row = s.split('=')
    d[int(row[0])] = row[1]
print(*sorted(d.items()))

#5=отлично
#4=хорошо
#3=удовлетворительно