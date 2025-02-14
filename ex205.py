'''
Подвиг 1. На вход программе подается строка с названиями городов, записанных через пробел. Необходимо прочитать эту
строку и применить функцию filter, которая бы возвращала только названия длиной более 5 символов. Извлеките первые
три полученных значения с помощью функции next и отобразите их на экране в одну строчку через пробел. (Полагается,
что минимум три значения имеются).
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.4.1
Sample Input:
Тула Ульяновск Хабаровск Владивосток Омск Уфа
Sample Output:
Ульяновск Хабаровск Владивосток
'''
cities = 'Тула Ульяновск Хабаровск Владивосток Омск Уфа'
new_c = filter(lambda x: len(x) > 5, cities.split())
for x in range(3):
    print(next(new_c), end=' ')