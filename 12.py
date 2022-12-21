
def dfdf():
    write1 = open(file="12,1.txt", mode="w")
    with open(file="12.txt", mode="r") as f:
        for line in f:
            if line.find('#') != -1:
                i = line.find('#')
                print(line[:i])
                continue
            elif line.find('!') != 0:
                j = line.find('!')
                print(line[:j])
                continue
            else:
                print(line)


dfdf()
