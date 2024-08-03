'''
Подвиг 7. На вход программе подается зашифрованное слово. Шифрование кодов символов этого слова было проведено
с помощью битовой операции XOR с ключом key=123. То есть, каждый символ был преобразован по алгоритму:
x = ord(x) ^ key
Здесь ord - функция, возвращающая код символа x. Прочитайте слово из входного потока и расшифруйте его. Выведите
на экран результат расшифровки.
P. S. Подсказка: для преобразования кода в символ используйте функцию chr.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.2.7
Sample Input:
ѩкю[щюлцхZ
Sample Output:
Все верно!
'''
a = 'ѩкю[щюлцхZ'
b = ''
key = 123
for x in a:
    b += chr(ord(x)^key)
print(b)
'''
Шпаргалка:
Проверка на включенность (1): if flags & mask == mask: # Бит включен (1)
Выключение бита: flags & ~mask
Включение бита: flags | mask
Переключение бита: flags ^ mask
Инверсия бит: ~number == -number - 1
Смещение бит вправо: number >> 1 == number // (2 ** 1)
Смещение бит влево: number << 1 == number * (2 ** 1)
'''