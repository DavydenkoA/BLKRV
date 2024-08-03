import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in =  ['А323ГД',
            'Д456ВВ',
            'Б001ББ',
            'Д456ВВ',
            'С111СС']
# здесь продолжайте программу (используйте список lst_in)
m = {x for x in lst_in}

print(len(m))