def get_rec_sum(n):
    #print(n)
    if len(n) == 0:  # Граничный случай
        return 0
    else:  # Рекурсивный случай
        return get_rec_sum(n[:-1]) + n[-1]


#greetings('Hello, world!')


a = [8, 11, -5, 4, 3]
get_rec_sum(a)
print(get_rec_sum(a))

# 8 11-5 4 3