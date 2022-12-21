def first_non_repeating_letter():
    a = list(input())
    for i in a:
        if a.count(i) > 1:
            a = [z for z in a if z != i]
        elif a.count(i) == 1:
            print(i)
            break


first_non_repeating_letter()
