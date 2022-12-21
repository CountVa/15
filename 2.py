def del_four_index():
    n = int(input("Введите количество символов списка: "))
    l = list()
    for b in range(n):
        a = int(input('Введите значение: '))
        if a % 4 == 0:
            continue
        else:
            l.append(a)
    print(l)
del_four_index()
