def pig_it():
    a = list(input())
    print(a)
    b = a[0]
    a.append(b)
    a.pop(0)
    for i in range(len(a)):
        if a[i] == ' ':
            a[i] = 'ay '
    for i in range(len(a)):
        if (a[-1] != '.') and (a[-1] != '?') and (a[-1] != '.'):
            a.append('ay')
            break
    zer = ''.join(a) # ''
    print(zer)

pig_it()
