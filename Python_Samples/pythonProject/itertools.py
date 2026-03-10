# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == '__main__':
    # S = input()
    S = "HACK 3"
    s = S.split()
    s1, k = sorted(s[0]), int(s[1])
    l = list(combinations_with_replacement(s1,k))
    for item in l:
        print("".join(item))