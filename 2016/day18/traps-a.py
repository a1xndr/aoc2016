input= ".^^.^.^^^^"
rows = 9
safe = 0
prevrow = list()
for c in input:
    prevrow.append(0 if c == "." else 1)
safe = prevrow.count(0)

for n in range(0, rows-1):
    row = list()
    for i in range(0, len(prevrow)):
        l = prevrow[i-1] if i >0 else 0
        c = prevrow[i]
        r = prevrow[i+1] if i < len(prevrow)-1 else 0
        row.append((c and ( l ^ r)) or ( (not c) and (l ^ r)))
    prevrow = row
    safe += prevrow.count(0)
    for c in row:
        print('^' if c else '.', end='')
    print()
print(safe)

    
