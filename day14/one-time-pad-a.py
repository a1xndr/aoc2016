import sys
import re
import numpy as np
import hashlib
salt = "jlmsuwbz"
m = hashlib.md5()
i = 0
sep = 1000
count = 0
lasthrees = dict()
rethree = re.compile(r"(.)\1{2}")
refive = re.compile(r"(.)\1{4}")
solns = set()
while(1):
    hsh = hashlib.md5((salt+str(i)).encode('utf-8')).hexdigest()
    threes = rethree.findall(hsh)
    fives = refive.findall(hsh)
    for m in fives:
        for n in lasthrees[m]:
            if(i-n <= sep):
                solns.add(n)
                count+=1
    if(threes != []):
        lasthrees.setdefault(threes[0], []).append(i)
    i+=1;
    if(count >= 69):
        break
j = 1
for i in sorted(solns):
    print(str(j)+" "+str(i))
    j+=1
    

