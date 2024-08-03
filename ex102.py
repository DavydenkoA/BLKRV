import sys

# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php']

# здесь продолжайте программу (используйте список lst_in)
menu = ()
for i in range(len(lst_in)):
    t = tuple(lst_in[i].split())
    menu += (t,)
print(menu)



# Главная home
# Python learn-python
# Java learn-java
# PHP learn-php