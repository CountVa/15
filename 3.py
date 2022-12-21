def contains_duplicates():
    n = int(input("Введите количество символов массива: "))
    l = list()
    for b in range(n):
        a = int(input('Введите значение: '))
        l.append(a)
    b = (set(l))
    print(b)
    if len(b) == n:
        print("True")
    else:
        print("False")
contains_duplicates()