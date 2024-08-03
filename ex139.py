t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

def get_str(str, sep='-'):
     out = ''
     for x in str:
          if x == ' ':
               x = sep
          if x in t:
               out += t.get(x)

          else:
               out += x
     return out


str = 'Лучший курс по Python!'
text_in = get_str(str.lower())
#text_in = get_str(input().lower())
print(text_in)
print(text_in.replace('-', '+'))


