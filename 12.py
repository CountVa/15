import re

def dfdf():
    read1 = open(file="12.txt", mode="r")
    write1 = open(file="12,1.txt", mode="w")
    info = read1.readline()
    i = info.find('#')
    zer = info[:i]
    print(zer)
dfdf()
