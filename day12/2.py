# What i've written is only going to be partially reusable for this I think
# Class for squares, total fences, tracked fences, fence north, fence east, fence west, fence south
# In find paths algo, pass x,y and char, plus direction
# Check this square for adjacencies and set total fences

# Does tracked fences = total fences? if so we've done this square, return

# set direction 90 left
# check for matching square - yes, and direction is not passed direction, add 1 to sides coount, , add 1 to tracked fences and update square with fence  direction-1 and call func, no, rotate 90 right, repeat
# return sides

import sys

class square:
    def __init__(self, c):
        self.char=c
    total=0
    tracked=0
    fences=[0,0,0,0] #nesw

class direction:
    def __init__(self,d):
        self.cur=d
    def left(self,d):
        d-=1
        if d<0: d+=4
        return d
    def right(self,d):
        d+=1
        if d>3: d-=4
        return d

class field:
    def __init__(self, a, s):
        self.sides = a
        self.area = s

def check_adj(x,y,s):
    char = s.char
    adj=0
    for sdir in sdirs:
        nx=x+sdir[0]
        if nx<0 or nx>xmax:
            adj+=1
            continue
        ny=y+sdir[1]
        if ny<0 or ny>ymax:
            adj+=1
            continue
        if grid[ny][nx].char!=char:
            adj+=1
    return adj



sdirs=[[0,-1],[1,0],[0,1],[-1,0]] #n,e,s,w


def find_paths(x,y,s,sdir):
#    print(x,y,f)
    if str(x)+"."+str(y) in visited:
        if s.char in visited[str(x)+"."+str(y)]:
            print("visited",x,y,s.char)
            if s.tracked==s.total:
                return 0,0
        else: visited[str(x)+"."+str(y)].append(s.char)
    else:
        visited[str(x)+"."+str(y)]=s.char
    #compute total sides for this square
    s.total = check_adj(x,y,s)
    sides=0
    squares=1
    print("finding ",s.char," next to ",x,y)
    d = direction(sdir)
    sdir=d.left(sdir)
    #think of a nicer way to maange directions here...
    for _ in range(3):
        nx=x+sdirs[sdir][0]
        if nx<0 or nx>xmax:
            s.fences[sdir]=1
            sdir=d.right(sdir)
            s.tracked+=1
            continue
        ny=y+sdirs[sdir][1]
        if ny<0 or ny>ymax:
            s.fences[sdir]=1
            sdir=d.right(sdir)
            s.tracked+=1
            continue
        if grid[ny][nx].char==s.char:
            print("found another ",s.char," at: ",nx,ny,sdir)
            if s.fences[d.left(sdir)]==0:
                sides+=1
            if grid[ny][nx].fences==1:
                sides-=1
            nadj,nsquares=find_paths(nx,ny,grid[ny][nx],sdir)
            sides+=nadj
            squares+=nsquares
        else:
            if s.fences[d.left(sdir)]==0:
                sides+=1
            sdir=d.right(sdir)
            s.tracked+=1
            s.fences[d.left(sdir)]=1
    return sides,squares

filename="input.txt"
if len(sys.argv)>1:
    filename=sys.argv[1]

f = open(filename)

visited={}
indexes={}
fields={}
grid=[]
y=0
for line in f.readlines():
    grid.append([])
    for char in line.strip():
        grid[y].append(square(char))
    y+=1
#print(grid)
xmax=len(grid[0])-1
ymax=len(grid)-1

index=0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        print ("testing:", x,y,grid[y][x].char)
        sides,squares=find_paths(x,y,grid[y][x],0)
        if sides>0 or squares>0:
            fields[grid[y][x].char+"."+str(index)]=field(sides,squares)
            index+=1
total=0
for f in fields:
    total+=fields[f].sides*fields[f].area
    print(f,fields[f].sides,fields[f].area,fields[f].sides*fields[f].area)

print ("Cost:",total)
