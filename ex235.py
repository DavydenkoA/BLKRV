'''
Подвиг 3. На вход программе подается целое десятичное число. Прочитайте его и, используя битовые операции, выключите
4-й и 1-й биты введенного числа. Выведите на экран полученное числовое значение.
P. S. Распределение номеров бит представлено на следующем рисунке.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.2.3
Sample Input:
153
Sample Output:
137
'''

# принимаем ввод целого числа
n = int(input())
# применяем операцию побитового И (AND) между значением переменной n и битовым отрицанием числа 0b10010
# битовое отрицание инвертирует каждый бит в числе, то есть меняет 0 на 1 и наоборот
res = n & ~0b10010
# выводим результат
print(res)
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