def sdad():
    a = set(input('введите слово '))
    z = int(input('massive '))
    be = list()
    b = list()
    for i in range(z):
        ze = list(input('v:'))
        b.append(ze)
        if (a.issubset(ze)) and (len(a) == len(ze)):
            be.append(ze)
    print(be)
sdad()