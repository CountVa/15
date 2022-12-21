def cakes():
    n = int(input("Введите количество символов словаря Рецепт: "))
    n1 = int(input("Введите количество символов словаря продукты: "))
    slov1 = {}
    slov2 = {}
    g = []
    g1 = []
    g2 = []
    a = 0
    b = 0
    for i in range(n):
        z = int(input("число1"))
        f = (input("слово1"))
        slov1[f] = z
        g.append(z)
    for i1 in range(n1):
        z1 = int(input("число2"))
        f1 = (input("слово2"))
        slov2[f1] = z1
        g1.append(z1)
    for i in range(len(g)):
        g2.append(g1[i] // g[i])
    print(min(g2))
    print(slov2, slov1)
cakes()

