# What i've written is only going to be partially reusable for this I think
# Class for squares, total fences, tracked fences, fence north, fence east, fence west, fence south
# In find paths algo, pass x,y and char, plus direction
# Check this square for adjacencies and set total fences

# Does tracked fences = total fences? if so we've done this square, return

# set direction 90 left
# check for matching square - yes, and direction is not passed direction, add 1 to sides coount, , add 1 to tracked fences and update square with fence  direction-1 and call func, no, rotate 90 right, repeat
# return sides

# What a tangled web I weave, I just can't get the above working
# New approach: find fences for each square, record their position and area they enclose
# Once finished analysing the grid, do a sequential pass both horizontally and vertically, tracking contiguous runs of fence (same Area and direction), incrementing sides per run

import sys

class square:
    def __init__(self, c):
        self.char=c
        self.total=0
        self.tracked=0
        self.fences=[0,0,0,0] #nesw

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
    def opp(self,d):
        d+=2
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


def find_paths(x,y,s,sdir,sides):
#    print(x,y,f)
    squares=0
    if str(x)+"."+str(y) in visited:
        if s.char in visited[str(x)+"."+str(y)]:
            print("visited",x,y,s.char)
            if s.tracked==s.total:
                return 0,0
        else:
            visited[str(x)+"."+str(y)].append(s.char)
    else:
        visited[str(x)+"."+str(y)]=s.char
        squares=1
    #compute total sides for this square
    s.total = check_adj(x,y,s)
    print("finding ",s.char," next to ",x,y)
    d = direction(sdir)
    sdir=d.left(sdir)
    #think of a nicer way to maange directions here...
    for _ in range(4):
        nx=x+sdirs[sdir][0]
        if nx<0:
            if grid[x][y+(sdirs[d.left(sdir)][1])].fences[sdir]!=1:
                sides+=1
            s.fences[sdir]=1
            sdir=d.right(sdir)
            s.tracked+=1
            continue
        if nx>xmax:
            if grid[x][y+(sdirs[d.left(sdir)][1])].fences[sdir]!=1:
                sides+=1
            s.fences[sdir]=1
            sdir=d.right(sdir)
            s.tracked+=1
            continue
        ny=y+sdirs[sdir][1]
        if ny<0:
            if grid[x+(sdirs[d.left(sdir)][0])][y].fences[sdir]!=1:
                sides+=1
            s.fences[sdir]=1
            sdir=d.right(sdir)
            s.tracked+=1
            continue
        if ny>ymax:
            if grid[x+(sdirs[d.left(sdir)][0])][y].fences[sdir]!=1:
                sides+=1
            s.fences[sdir]=1
            sdir=d.right(sdir)
            s.tracked+=1
            continue
        if grid[ny][nx].char==s.char:
            if x>0 and x<xmax or y>0 and y<ymax:
                print("checking ",sdirs[d.opp(sdir)][0],sdirs[d.opp(sdir)][1],d.left(sdir))
                if grid[x+sdirs[d.opp(sdir)][0]][y+sdirs[d.opp(sdir)][1]].fences[d.left(sdir)]==0:
                    sides+=1
#            if grid[ny][nx].fences[d.left(sdir)]==1:
#                sides-=1
            print("found another ",s.char," at: ",nx,ny,sdirs[sdir]," sides:",sides,"fences",s.fences)
            sides,nsquares=find_paths(nx,ny,grid[ny][nx],sdir,sides)
#            sides+=nadj
            squares+=nsquares
        else:
            if x>0 and x<xmax or y>0 and y<ymax:
                if grid[x+(sdirs[d.opp(sdir)][0])][y+(sdirs[d.opp(sdir)][1])].fences[sdir]!=1:
                    sides+=1
                elif grid[x-(sdirs[d.opp(sdir)][0])][y-(sdirs[d.opp(sdir)][1])].fences[sdir]==1:
                    sides-=1
            s.fences[sdir]=1
            sdir=d.right(sdir)
            s.tracked+=1
    print("total fences for ",x,y,":",s.total," we've processed",s.tracked,sum(s.fences))
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
        sides,squares=find_paths(x,y,grid[y][x],0,0)
        if sides>0 or squares>0:
            fields[grid[y][x].char+"."+str(index)]=field(sides,squares)
            index+=1
total=0
for f in fields:
    total+=fields[f].sides*fields[f].area
    print(f,fields[f].area,fields[f].sides,fields[f].sides*fields[f].area)

print ("Cost:",total)
