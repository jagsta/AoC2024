import sys

class field:
    def __init__(self, a, s):
        self.adj = a
        self.area = s

sdirs=[[0,-1],[1,0],[0,1],[-1,0]] #n,e,s,w


def find_paths(x,y,f):
#    print(x,y,f)
    if str(x)+"."+str(y) in visited:
        if f in visited[str(x)+"."+str(y)]:
            print("visited",x,y,f)
            return 0,0
        else: visited[str(x)+"."+str(y)].append(f)
    else: visited[str(x)+"."+str(y)]=f
    adj=0
    squares=1
    print("finding ",f," next to ",x,y)
    for sdir in sdirs:
        #bounds check
        nx=x+sdir[0]
        if nx<0 or nx>xmax:
            adj+=1
            continue
        ny=y+sdir[1]
        if ny<0 or ny>ymax:
            adj+=1
            continue
        if grid[ny][nx]==f:
            print("found another ",f," at: ",nx,ny)
            nadj,nsquares=find_paths(nx,ny,f)
            adj+=nadj
            squares+=nsquares
        else:
            adj+=1
    return adj,squares

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
        grid[y].append(char)
    y+=1
print(grid)
xmax=len(grid[0])-1
ymax=len(grid)-1

index=0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        print ("testing:", x,y,grid[y][x])
        adj,squares=find_paths(x,y,grid[y][x])
        if adj>0 or squares>0:
            fields[grid[y][x]+"."+str(index)]=field(adj,squares)
            index+=1
total=0
for f in fields:
    total+=fields[f].adj*fields[f].area
    print(f,fields[f].adj,fields[f].area,fields[f].adj*fields[f].area)

print ("Cost:",total)
