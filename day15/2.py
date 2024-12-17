import sys
import re

class robot:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def look(self,x,y):
        nx=x+self.dx
        ny=y+self.dy
        n=grid[ny][nx]
#        print(n,nx,ny)
        if n=="O":
            self.m.append([nx,ny])
            r=self.look(nx,ny)
            return r
        if n=="#":
            return 0
        if n==".":
            self.m.append([nx,ny])
            return 1

    def move(self,d):
        self.dx=sdirs[d][0]
        self.dy=sdirs[d][1]
        self.m=[]
        canmove=self.look(self.x,self.y)
        if canmove==1:
            return self.m
        elif canmove==0:
            return [[-1,-1]]


sdirs={"^":[0,-1],">":[1,0],"v":[0,1],"<":[-1,0]}

filename="input.txt"

if len(sys.argv)>1:
    filename=sys.argv[1]

f = open(filename)

r=None
moves=""
grid=[]
y=0
x=0
for line in f.readlines():
    match=re.match(r'(<|\^|>|v)+',line)
    if match:
        moves+=line.strip()
    elif len(line)>1:
        grid.append([])
        x=0
        for c in line.strip():
            if c=="@":
                r=robot(x,y)
            grid[y].append(c)
            x+=1
        y+=1

xmax=len(grid[0])-1
ymax=len(grid)-1
print(grid)
print(moves)
print(r.x,r.y,xmax,ymax)

for m in moves:
    updates=r.move(m)
#    print(m,updates)
    if updates[0]!=[-1,-1]:
        for update in reversed(updates):
            grid[update[1]][update[0]]=grid[update[1]-sdirs[m][1]][update[0]-sdirs[m][0]]
        grid[r.y][r.x]="."
        r.x=r.x+sdirs[m][0]
        r.y=r.y+sdirs[m][1]

#    for line in grid:
#        print(line)

total=0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x]=="O":
            total+=(100*y)+x

print(total)
