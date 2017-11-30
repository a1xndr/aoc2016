pat = [1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1]
size = len(pat)
target = 35651584
def flip(li):
    fl = list()
    for i in li:
        fl.append(int(not i))
    return fl[::-1] 
while(size<target):
    fl = flip(pat)
    pat = pat + [int(0)] + fl
    size+=size+1
pat = pat[0:target]
while(1):
    li = list();
    for a, b in zip(pat[::2], pat[1::2]):
        li.append(int(not (a ^ b)));
    if(len(li)%2 == 1):
        print("".join(map(str,li)))
        break
    pat = li;


