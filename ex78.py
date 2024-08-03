import sys

# считывание списка из входного потока

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
[print(*x[::-1],end = ' ') for x in lst_in[::-1]]


# 1 2 3 4
# 5 6 7 8
# 9 8 7 6
# 5 4 3 2