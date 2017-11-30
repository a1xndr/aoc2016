import sys
import re
import numpy as np



def main():
    dvec = { 'R': [1, 0], 'L': [-1, 0], 'U': [0, 1] , 'D': [0, -1]}
    f = open("input" , "r")
    for line in f:
        s = line.rstrip()
        p = 5
        for c in s:
            r = ceil(sqrt(p))
            c = ceil(sqrt(p))
            t = p + dvec[c][0] - 3*dvec[c][1]
            if t > 0 and t < 10 and ((int((t-1)/3) == int((p-1)/3)) or c == "U" or c =="D") :
                p = t
        print(p)

if __name__ == "__main__":
    main()
