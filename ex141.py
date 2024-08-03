def get_tag(str_in, tag='div', up=True):
    if up == True:
        return f"<{tag.upper()}>{str_in}</{tag.upper()}>"
    else:
        return f"<{tag}>{str_in}</{tag}>"

str_in = 'Python is best!'
out = get_tag(str_in)
#out = get_tag(input())

print(get_tag(str_in, 'div'))
print(get_tag(str_in, 'div', False))