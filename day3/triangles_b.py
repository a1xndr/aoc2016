import sys
import re
import numpy as np

def main():
    count = 0 
    f = open("input" , "r")
    cols = list()
    for i in range(0, 2):
        cols.append(list())
    for line in f:
        line = list(line.rstrip().split())
        for i in range(0, 2):
            cols[i].append(int(line[i]))
            if(len(cols[i]) >= 3):
                print("D: " + str(sorted(cols[i])) )
                if sorted(cols[i])[0] + sorted(cols[i])[1] > sorted(cols[i])[2] :
                    print(str(cols[i][0]) +" "+ str(cols[i][1])+" " + str(cols[i][2]) )
                    count += 1
                cols[i] = cols[i].pop(0)
    print(count)
if __name__ == "__main__":
    main()
