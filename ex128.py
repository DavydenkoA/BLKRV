def is_triangle(a, b, c):
    if a < (b + c) and b < (c + a) and c < (b + a):
        return True
    else:
        return False

#a, b, c = map(int, input().split())