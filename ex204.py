'''
Подвиг 6. На вход программе подается строка с названиями городов, записанных в одну строчку через пробел. Необходимо
ее прочитать и применить функцию map так, чтобы она возвращала названия городов только длиной более 5 символов.
Вместо остальных названий - строку с дефисом ("-"). Сформировать список из полученных значений и отобразить его на
экране в одну строчку через пробел.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.3.6
Sample Input:
Москва Уфа Вологда Тула Владивосток Хабаровск
Sample Output:
Москва - Вологда - Владивосток Хабаровск
'''
cities = 'Москва Уфа Вологда Тула Владивосток Хабаровск'
new_c = list(map(lambda x: ('-', x)[len(x) > 5], cities.split()))
print(*new_c)