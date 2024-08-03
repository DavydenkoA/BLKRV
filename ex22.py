a, b, c = map(int, input().split())
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
d = (m[a-1]) if  a > 0 else False
e = (m[b-1]) if  a > 0 else False
f = (m[c-1]) if  a > 0 else False

print('#' + d if d == 'до' or d == 'фа' else d, '#' + e if e == 'до' or e == 'фа' else e, '#' + f if f == 'до' or f == 'фа' else f)

# 1 6 7