def createDict():
    z = dict()
    a = list()
    b = list()
    i = int(input())
    j = int(input())
    for k in range(0, i):
        r1 = input()
        a.append(r1)
    for f in range(0, j):
        r2 = input()
        b.append(r2)
    if len(b) == len(a):
        for g in range(len(b)):
            z[b[g]] = a[g]
    if len(b) > len(a):
        for g in range(len(a)):
            z[b[g]] = a[g]
        for g in range(len(a), len(b)):
            z[b[g]] = 'None'
    if len(b) < len(a):
        for g in range(len(b)):
            z[b[g]] = a[g]
        for g in range(len(b), len(a)):
            break
    print(z)
createDict()
