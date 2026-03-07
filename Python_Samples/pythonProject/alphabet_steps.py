#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calculateMinSteps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING inputStr as parameter.
#
import string


def calculateMinSteps(inputStr):
    #alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = string.ascii_uppercase
    alpha_dict = {item: index+1 for index, item in enumerate(alpha)}

    counter = 0
    item1 = inputStr[0]
    item2 = ""

    for index in range(1, len(inputStr)):
        item2 = inputStr[index]
        maximum, minimum = max(alpha_dict[item1], alpha_dict[item2]), min(alpha_dict[item1], alpha_dict[item2])

        # forward and reverse
        f = 26 - maximum + minimum
        r = maximum - minimum

        counter += min(f, r)
        item1 = item2

    return counter


inputStr = "AZGB"
print(calculateMinSteps(inputStr))




