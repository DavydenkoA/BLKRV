s = input().split()  # ввод данных 'one=1','two=2','three=3'
lst = [s[i].split('=') for i in range(len(s))] # разбивка данных .,через list comprehension [s[элемент].split('=') пробегаемся по длинне списка (всего 3 элемента)].Таким образом у нас сейчас данные получаются 'one' '1' и т.д.
d = dict(lst)        # делаем словарь
for key in d:        # цикл чтобы получить пару строка : число
    d[key] = int(d[key])
print(*sorted(d.items()))

# one=1 two=2 three=3
# one, 1