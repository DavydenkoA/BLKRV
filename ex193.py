# Считываются значения a и b с помощью input() и map().
a,b = map(int,input().split())
# Определяется функция f(x), которая вычисляет значение функции в точке x.
def f(x):
    return 0.5 * pow(x, 2) - 2.0
# Создается генератор gen, который выдает значения x с шагом 0.01 в диапазоне от 100a до 100b.
gen = ((x/100) for x in range(100*a,100*b))
# Создается список lst, который содержит значения функции f(x) для каждого значения x из генератора gen.
# Значения округляются до сотых.
lst = [round(f(x),2) for x in gen]
# На экран выводятся первые 20 значений списка lst.
print(*lst[0:20])