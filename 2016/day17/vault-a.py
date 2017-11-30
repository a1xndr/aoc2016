import hashlib

input = "pvhmgsws"
dirs = ['U', 'D', 'L', 'R']

q = list()
hsh = list(hashlib.md5(input.encode('utf-8')).hexdigest())
print(''.join(hsh))
for d in range(0, 4):
    if( ord(hsh[d]) > ord('f') or ord(hsh[d]) < ord('b')):
        continue;
    else:
        q.append(dirs[d])

for path in q:
    print("at " + path  + " in " + str(q))
    y = list(path).count('D') - list(path).count('U')
    x = list(path).count('R') - list(path).count('L')
    print("x: " + str(x))
    print("y: " + str(y))
    if(not (0 <= y < 4)):
        continue
    if(not (0 <= x < 4)):
        continue
    if( y == 3 and x == 3 ):
        print(path)
        break
    hsh = list(hashlib.md5((input+path).encode('utf-8')).hexdigest())
    print(''.join(hsh))
    for d in range(0, 4):
        if( ord(hsh[d]) > ord('f') or ord(hsh[d]) < ord('b')):
            continue;
        else:
            q.append(path+dirs[d])
    print()

