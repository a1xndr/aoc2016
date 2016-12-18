import sys
import re
import numpy as np

def main():
    visited = dict()
    f = open("input" , "r")
    for line in f:
        s = line
    f.close()
    moves = s.split(", ")
    p = np.array([0, 0])
    d = np.array([0, 1, 0, -1])
    for m in moves:
        d = np.roll(d, (1, -1)[m[0]=="R"])
        dist = int(re.findall('\d+', m)[0])
        for n in range(0, dist):
            p = np.add(p, d[0:2])
            if tuple(p) in visited:
                print("Intersect" )
                print(abs(p[0])+abs(p[1])) 
                return 0
            visited[tuple(p)] = 1

    print(abs(p[0])+abs(p[1]))

if __name__ == "__main__":
    main()
