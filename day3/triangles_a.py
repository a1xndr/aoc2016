import sys
import re
import numpy as np

def main():
    count = 0 
    f = open("input" , "r")
    for line in f:
        s = sorted([int(i) for i in list(line.rstrip().split())])
        if s[0] + s[1] > s[2] :
            count += 1
    print(count)
if __name__ == "__main__":
    main()
