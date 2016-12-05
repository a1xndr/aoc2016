f = open("input" , "r")
cols = list()
n = 0;
count = 0 
for i in range(0, 3):
    cols.append(list())
for line in f:
    n+=1
    line = list(line.rstrip().split())
    for i in range(0, 3):
        cols[i].append(int(line[i]))
        if(n%3 == 0):
            if sorted(cols[i])[0] + sorted(cols[i])[1] > sorted(cols[i])[2] :
                count += 1
        if(n>=3):
            cols[i].pop(0)
print(count)
