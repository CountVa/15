def sum_digit():
    try:
        a = int(input('Введите целое число: '))
        z = 0
        l = []
        while True:
            if a / 10 != 0:
                z = z + (a % 10)
                a = a // 10
            else:
                break
        print(z)
    except ValueError:
        print("Некорректный тип данных!")
sum_digit()