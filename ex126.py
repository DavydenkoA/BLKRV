def send_email(mail):
    #e_box = input()
    t = set("abcdefghijklmnopqrstuvwxyz0123456789_@.")
    for i in mail:
        if '@' not in mail or '.' not in mail or '_' not in mail:
            print('НЕТ')
            break
        if i.lower() in t:
            True
        else:
            print('НЕТ')
            break
    else:
        print('ДА')


send_email(input())


# sc_lib@list.ru
# sc_liblist.ru