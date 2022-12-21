x = 'k3e10g88f13'
word =[]
number = []
for i in x:
    if i.isalpha():
        word.append(i)
    else:
        number.append(i)
print(word, number,sep="\n")