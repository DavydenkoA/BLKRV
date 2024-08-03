a = list(input(). casefold()) #не учитываем регистр
b = a[::-1]
msg = 'палиндром' if b == a else 'не палиндром'
print(msg)


# Казак