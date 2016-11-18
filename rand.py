import random


def getRand(n):
    randInts = []
    for x in range(0, n):
        randInts.append(random.randint(1, 6))
    return(randInts)

def attribute():
    rolls = sorted(getRand(4))
    del rolls[0]
    attrib = sum(rolls)
    return(attrib)

attrib = attribute()
##print(attrib)
