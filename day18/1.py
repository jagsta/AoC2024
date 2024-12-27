import sys

file="input.txt"
gridmax=70

if len(sys.argv)>1:
    file=sys.argv[1]
    gridmax=6

f=open(file)

grid= [["." for x in range(gridmax)] for y in range(gridmax)]
for line in grid:
    s=""
    for c in line:
        s+=c
    print(s)

limit=1024
i=0
while i<limit:
    line=f.readline()
    i+=1
