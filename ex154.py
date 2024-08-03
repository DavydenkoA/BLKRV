# ввод числа N
N = int(input())

# здесь задается функция fib_rec (переменную N не менять!)
#N = int(input())

def fib_rec(N, f=[1, 1]):
    if len(f) < N:
        f.append(f[-1] + f[-2])
        fib_rec(N, f)
    return f


print(fib_rec(N))
