import sys
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
for x, str in enumerate(lst_in):
    while str.count('  '):
        str = str.replace('  ', ' ')
    print(str.replace(' ', '-'), end='')
    print()


# django chto  eto takoe    poryadok ustanovki
# model mtv   marshrutizaciya funkcii  predstavleniya
# marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya