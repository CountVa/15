
def dfdf():
    write1 = open(file="12,1.txt", mode="w")
    with open(file="12.txt", mode="r") as f:
        for line in f:
            if line.find('#') != 0:
                i = line.find('#')
                print(line[:i])
            elif line.find('!') != 0:
                j = line.find('!')
                print(line[:j])
            else:
                print(line)


dfdf()
