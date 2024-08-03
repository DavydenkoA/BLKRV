number = input()
cat = list(number)
symbols = ('+' '(' ')' '-')
correct = []

if len(cat) != 16 or cat[0] != '+' or cat[1] != '7' or cat[2] != '(' or cat[6] != ')' or cat[10] != '-' or cat[13] != '-':
    print('НЕТ')
else:
    for i in range(0, 16):
        if number[i] in symbols:
            cat.remove(number[i])
            continue
        elif number[i] not in symbols:
            correct.append(number[i])
            strings = ''.join(correct)
    if strings.isdigit():
        print('ДА')
    else:
        print('НЕТ')


# +7(123)456-78-99