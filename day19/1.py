import functools
import sys
import re

@functools.cache
def fit2(string):
    found=False
    if string=="":
        return True
    sub=""
    while len(sub)<=lmax and len(string)>len(sub) and not found:
        sub+=string[len(sub)]
#        print("looking for",sub,"in",lstring)
        for t in towels:
            if sub in towels and not found:
#                print("found",sub,"in",string,"remains",string[len(sub):])
                #found a match for this substring, check for remainder of string
                found=fit2(string[len(sub):])
    return found


file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

towels=set()
patterns=[]
for line in f.readlines():
    match=re.match(r'\w+,',line)
    if match:
        towel=line.strip().split(", ")
        for t in towel:
            towels.add(t)
    elif len(line)>1:
        patterns.append(line.strip())
lmax=0
lmin=100
for t in towels:
    if len(t)>lmax:
        lmax=len(t)
    elif len(t)<lmin:
        lmin=len(t)
print(lmin,lmax)
print(len(towels))
print(towels)
print(patterns)
matches=0
for p in patterns:
    found=fit2(p)
    if found:
        print("Found pattern for",p)
        matches+=1
    else:
        print("No pattern for",p)

print(matches)
