def get_data_fig(*args, **kwargs):
    t = []
    t.append(sum(args))
    if 'type' in kwargs:
        t.append(kwargs.get('type'))
    if 'color' in kwargs:
        t.append(kwargs.get('color'))
    if 'closed' in kwargs:
        t.append(kwargs.get('closed'))
    if 'width' in kwargs:
        t.append(kwargs.get('width'))
    print(tuple(t)) # для решения задачи return
    #print(kwargs.get('type'))


get_data_fig(2, 18, 10, type=True, color=14, closed=True, width=12)