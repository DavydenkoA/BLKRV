import sys
# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
result = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))] # В внешнем списке (i) за размер берем длину
# одного вложенного цикла, в внутренним берем из каждого вложенного цикла индекс i и сохраняем в наш вложенный список.
for row in result:
    print(*row)
# здесь продолжайте программу (используйте список lst_in)


# 1 2 3
# 4 5 6
# 7 8 9
# 5 4 3