# We need to find when all ( p + n + x ) % s = 0 where p is initial position
# n is depth, x is time delay and s is number of steps
discs = [
        [13, 1],
        [19, 10],
        [3, 2],
        [7, 1],
        [5, 3],
        [17, 5],
        [11, 0]
        ]
x = 0
while(1):
    f = 0
    for idx, row in enumerate(discs):
        if( (row[1]+idx+1+ x) % row[0] != 0):
            f = 1
            break;
    if(f == 0):
        print(x)
        break;
    x+=1

