import sys

# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [
    "ustanovka-i-zapusk-yazyka",
"ustanovka-i-poryadok-raboty-pycharm",
"peremennyye-operator-prisvaivaniya-tipy-dannykh",
"arifmeticheskiye-operatsii",
"ustanovka-i-poryadok-raboty-pycharm"
          ]

# здесь продолжайте программу (используйте список lst_in)
d = {}
URL = 'URL'
d[URL] = []
URL_word = {'One': "HTML-страница для адреса", 'Two': "Взято из кэша: HTML-страница для адреса"}
n = 0
for x in lst_in:
    d[URL].append(x)
    if x in d['URL'][:-1]:
        print(URL_word['Two'], d['URL'][n])
    else:
        print(URL_word['One'], d['URL'][n])

    n += 1

    # print(x)
    # print(d)



