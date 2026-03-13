def findSmallestMissingPositive(orderNumbers):
    # Write your code here
    if orderNumbers == []:
        return 1
    orderNumbers.sort()
    new_list = [x for x in orderNumbers if x >= 0]
    if new_list == []:
        return 1
    minimum = min(new_list)
    maximum = max(new_list)
    for x in range(minimum,maximum+2):
        if x not in new_list:
            return x
    return maximum + 1

#orderNumbers = [3, 4, -1, 1]
#orderNumbers = [-2, -2, -2, -2, -2]
#orderNumbers = [3, 4, 5, 2]
orderNumbers = [2, -3, 4, 1, 1, 7]
#orderNumbers = [5, 3, 2, 5, 1]
#orderNumbers = [-8, 0, -1, -4, -3]
print(findSmallestMissingPositive(orderNumbers))