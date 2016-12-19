input = ".^^.^.^^^^"
rows = 10
safe = 0
prevrow = list()
for c in input:
    prevrow.append(0 if c = "." else 1)
safe = prevrow.count(0)

for n in range(0, rows):
    for i in range(0, len(prevrow)):
        l = prevrow[i-1] if i >0 else 0
        c = prevrow[i]
        r = prevrow[i+1] if i < len(prevrow)-1 else 0
        row = prevrow
    
