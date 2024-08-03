import sys

# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Мария',
          'Елена',
          'Екатерина',
          'Александр',
          'Елена',
          'Мария']


# здесь продолжайте программу (используйте список lst_in)
mnzh = set(lst_in)
print(len(mnzh))