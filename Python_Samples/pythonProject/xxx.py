def getMaxDisjointIntervals(l, r):
    # Write your code here
    counter = 1
    l3 = list(zip(l, r))
    l3 = sorted(l3, key=lambda x: x[0])
    print(l3)
    i1, f1 = l3[0]
    # for i, f in zip(l,r):
    for i2, f2 in l3[1:]:
        if f1 <= i2:
            counter += 1
            i1, f1 = i2, f2
    return counter


l = [6, 4, 1, 3, 8, 11, 7]
r = [9, 6, 4, 7, 13, 16, 8]
print(getMaxDisjointIntervals(l, r))
