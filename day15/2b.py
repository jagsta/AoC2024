import sys
import re

class robot:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def look(self,x,y,d,depth):
        nx=x+self.dx
        ny=y+self.dy
        n=grid[ny][nx]
        self.m.append([])
        print(n,nx,ny)
#       TODO: Need to index depth of search, add a new index of lists for each time we recurse, append to that index. This should preserve order?
        if n=="[" or n=="]":
            if d=="^" or d=="v":
                if n=="[":
                    if [nx,ny] not in self.m[depth]:
                        self.m[depth].append([nx,ny])
                    if [nx+1,ny] not in self.m[depth]:
                        self.m[depth].append([nx+1,ny])
                    p=self.look(nx,ny,d,depth+1)
                    q=self.look(nx+1,ny,d,depth+1)
                elif n=="]":
                    if [nx-1,ny] not in self.m[depth]:
                        self.m[depth].append([nx-1,ny])
                    if [nx,ny] not in self.m[depth]:
                        self.m[depth].append([nx,ny])
                    p=self.look(nx,ny,d,depth+1)
                    q=self.look(nx-1,ny,d,depth+1)
                if p and q:
                    return 1
                else:
                    return 0
            else:
                self.m[depth].append([nx,ny])
                r=self.look(nx,ny,d,depth+1)
            return r
        if n=="#":
            return 0
        if n==".":
            self.m[depth].append([nx,ny])
            return 1

    def move(self,d):
        self.dx=sdirs[d][0]
        self.dy=sdirs[d][1]
        self.m=[]
        depth=0
        canmove=self.look(self.x,self.y,d,depth)
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
            if c=="#" or c==".":
                grid[y].append(c)
                grid[y].append(c)
            if c=="O":
                grid[y].append("[")
                grid[y].append("]")
            if c=="@":
                grid[y].append(c)
                grid[y].append(".")
                r=robot(x,y)
            x+=2
        y+=1

xmax=len(grid[0])-1
ymax=len(grid)-1
for l in grid:
    print(l)
print(moves)
print(r.x,r.y,xmax,ymax)

for m in moves:
    updates=r.move(m)
    for u in updates:
        print(u)
    print(m,updates[0])
    if updates[0]!=[-1,-1]:
        for i in reversed(range(len(updates))):
            for update in updates[i]:
                if i>0:
                    print("layer",i,update,"checking",update[0]-sdirs[m][0],update[1]-sdirs[m][1],"in",updates[i-1])
                    if [update[0]-sdirs[m][0],update[1]-sdirs[m][1]] in updates[i-1]:
                        print("matched in layer below")
#                print(update,update[0]-sdirs[m][0],update[1]-sdirs[m][1])
                        square=grid[update[1]-sdirs[m][1]][update[0]-sdirs[m][0]]
                        grid[update[1]][update[0]]=square
                    else:
                        grid[update[1]][update[0]]="."
                else:
                    grid[update[1]][update[0]]="."
        grid[r.y][r.x]="."
        r.x=r.x+sdirs[m][0]
        r.y=r.y+sdirs[m][1]
        grid[r.y][r.x]="@"
#        for update in updates:
#            if grid[update[1]][update[0]]=="[" and grid[update[1]][update[0]+1]!="]":
#                grid[update[1]][update[0]]="."
#            if grid[update[1]][update[0]]=="]" and grid[update[1]][update[0]-1]!="[":
#                grid[update[1]][update[0]]="."
    else:
        print("can't move,skipping")
    for line in grid:
        string=""
        for c in line:
            string+=c
        print(string)

total=0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x]=="[":
            total+=(100*y)+x

print(total)
