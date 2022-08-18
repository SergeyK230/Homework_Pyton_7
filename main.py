import controller as cont

flag = True
while flag:
    cont.start()
    vvod = input('Введите любой ключ чтобы продолжить или N чтобы выйти -> ')
    if vvod == 'N' or vvod == 'n':
        flag = not flag
