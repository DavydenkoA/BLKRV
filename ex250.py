'''
Подвиг 7. В функцию get_data() передается параметр value:
def get_data(value):
    match value:
        # здесь продолжайте программу
    return None
Необходимо дописать оператор match/case со следующими шаблонами:
если переменная value имеет тип int и больше нуля, то вернуть значение переменной value;
если переменная value имеет тип float и находится в диапазоне [-100; 100], то вернуть значение переменной value;
если переменная value имеет тип str, то просто вернуть ее значение.
P. S. Вызывать функцию не нужно, только дописать шаблоны.
'''
def get_data(value):
    match value:
        case int() as command if command > 0:
            return command
        case float() as command if -100 < command < 100:
            return command
        case str() as command:
            return command

    return None