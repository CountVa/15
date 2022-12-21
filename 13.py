def check_p():
    a = list(input())
    if a.count('(') == a.count(")"):
        j = 0
        try:
            while j != range(len(a)):
                if (a[j] == "(") and (a[j + 1] == ")"):
                    a.pop(j)
                    a.pop(j)
                    j = 0
                else:
                    j += 1

        except:
            if (len(a)) == 0:
                print('true')
            else:
                print('false')

    else:
        print('false')
check_p()

