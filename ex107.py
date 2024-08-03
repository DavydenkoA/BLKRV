import sys

# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['EvgeniyK: спасибо большое!', 'LinaTroshka: лайк и подписка!',
          'Sergey Karandeev: крутое видео!', 'Евгений Соснин: обожаю',
          'EvgeniyK: это повтор?', 'Sergey Karandeev: нет, это новое видео']
# здесь продолжайте программу (используйте список lst_in)
lst_on = []
for x, d in enumerate(lst_in):
    pos = d.index(':')
    lst_on.append(d[0:pos])
mnzh = set(lst_on)
print(len(mnzh))


