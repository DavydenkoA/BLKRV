def get_tag(str, tag='h1'):
    return f"<{tag}>{str}</{tag}>"

str_in = 'Работаем с функциями'
out = get_tag(str_in)
#out = get_tag(input())

print(out)
print(out.replace('h1', 'div'))