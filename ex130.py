def get_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


a = int(input())

while a != 1:
    if get_even(a):
        print(a)
    a = int(input())