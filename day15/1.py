import sys
import re

filename="input.txt"

if len(sys.argv)>1:
    filename=sys.argv[1]

f = open(filename)

moves=""
grid=[]
i=0
for line in f.readlines():
    match=re.match(r'(<|\^|>|v)+',line)
    if match:
        moves+=line.strip()
    elif len(line)>1:
        grid.append([])
        for c in line.strip():
            grid[i].append(c)
        i+=1

print(grid)
print(moves)
