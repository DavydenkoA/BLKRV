weight = int(input()) * 1000
lst = []
gram = 0
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
things = sorted(things.items(), key=lambda item: item[1], reverse=True)

for x in things:
    gram += x[1]
    if gram <= weight:
        lst.append(x[0])
    else:
        gram -= x[1]

print(*lst)