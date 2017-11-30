import time
f = open('input', 'r')
lines = f.readlines()
pos = 0
reg = {"a":0, "b":0, "c":1, "d":0}
while(pos < len(lines)):
    line = lines[pos]
    print(str(pos)+"  " +line, end="")
    cmd = line[:3]
    if(cmd == "cpy"):
        orig = line.split()[1]
        dest = line.split()[2]
        if(orig.isalpha()):
            reg[dest]=reg[orig]
        else:
            reg[dest]=int(orig)
    elif(cmd == "inc"):
        dest = line.split()[1]
        reg[dest]+=1
    elif(cmd == "dec"):
        dest = line.split()[1]
        reg[dest]-=1
    elif(cmd == "jnz"):
        cond = line.split()[1]
        delta = int(line.split()[2])
        if(cond.isalpha()):
            cond=reg[cond]
        if(int(cond) != 0):
            pos += delta-1;
    print(str(pos)+" a " +str(reg["a"]))
    print(str(pos)+" b " +str(reg["b"]))
    print(str(pos)+" c " +str(reg["c"]))
    print(str(pos)+" d " +str(reg["d"]))
    print()
    pos+=1;


