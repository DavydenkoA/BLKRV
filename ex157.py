def get_path(N):      # объявляем функцию, которая принимает число
    count = 0         # переменная счетчик
    if N == 0:        # если ввели - 0, то она никуда не сдвинется и останется в той же точке
        return count
    elif N == 1:      # если ввели 1, то есть только 1 вариант туда попасть
        return count + 1
    elif N == 2:      # если ввели 2, то есть только 2 варианта туда попасть
        return count + 2
    else:             # иначе возвращем сумму от вызова функций с уменьшенным числом на 1 и на 2
        return get_path(N-1) + get_path(N-2)
#вызов функции
end = int(input())
print(get_path(end))