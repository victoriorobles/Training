def asterics1(level):
    aste = '*'
    blank = "-"
    for i in range(1,level+1):
        print(aste*(level-i))


def asterics2(level):
    aste = '*'
    blank = "-"
    for i in range(1,level+1):
        print(aste*(level-(level-i)))


def asterics3(level):
    aste = '*'
    blank = "-"
    for i in range(1,level+1):
        print(blank * (level-i) + aste * (level - (level - i)))

def asterics4(level):
    aste = '*'
    blank = "-"
    for i in range(1,level+1):
        print(blank*(level-(level-i)) + aste * (level-i))



asterics1(10)
asterics2(10)
asterics3(10)
asterics4(10)
