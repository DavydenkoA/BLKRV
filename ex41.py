import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

i = 0
while i < len(lst_in):
    if ' ' in lst_in[i]:
        lst_in.pop(i)
    else:
        i += 1
print(*lst_in)

#Муму
#Евгений Онегин
#Сияние
#Мастер и Маргарита
#Пиковая дама
#Колобок