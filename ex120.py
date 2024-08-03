import sys

# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Пушкин: Сказака о рыбаке и рыбке', 'Есенин: Письмо к женщине',
          'Тургенев: Муму', 'Пушкин: Евгений Онегин', 'Есенин: Русь']
# здесь продолжайте программу (используйте список lst_in)

m = [x.split(":") for x in lst_in]

d = {avtor[0]: {proiz[1].lstrip() for proiz in m if proiz[0] == avtor[0]} for avtor in m}

print(d)