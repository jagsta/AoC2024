import sys

class field:
    def __init__(self, a, s):
        self.adj = a
        self.area = s

sdirs=[[0,-1,"n"],[1,0,"e"],[0,1,"s"],[-1,0,"w"]] #n,e,s,w
cdir=["n","e","s","w"]


def find_paths(x,y,f,side):
#    print(x,y,f)
    if str(x)+"."+str(y) in visited:
        if f in visited[str(x)+"."+str(y)]:
            print("visited",x,y,f)
            side={}
            return 0,0,side
        else:
            visited[str(x)+"."+str(y)].append(f)
    else: visited[str(x)+"."+str(y)]=f
    adj=0
    squares=1
    print("finding ",f," next to ",x,y)
    for sdir in sdirs:
        #bounds check
        nx=x+sdir[0]
        if nx<0 or nx>xmax:
            adj+=1
            side[(str(x)+"."+str(y)+"."+sdir[2])]=f
            continue
        ny=y+sdir[1]
        if ny<0 or ny>ymax:
            adj+=1
            side[(str(x)+"."+str(y)+"."+sdir[2])]=f
            continue
        if grid[ny][nx]==f:
            print("found another ",f," at: ",nx,ny)
            nside={}
            nadj,nsquares,nside=find_paths(nx,ny,f,nside)
            adj+=nadj
            side = side | nside
            squares+=nsquares
        else:
            adj+=1
            side[(str(x)+"."+str(y)+"."+sdir[2])]=f
    return adj,squares,side

filename="input.txt"
if len(sys.argv)>1:
    filename=sys.argv[1]

f = open(filename)

fences={}
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
        side={}
        print ("testing:", x,y,grid[y][x])
        adj,squares,side=find_paths(x,y,grid[y][x],side)
        if adj>0 or squares>0:
            fields[grid[y][x]+"."+str(index)]=field(adj,squares)
            for s in side:
                side[s]+="."+str(index)
            fences = fences | side
            index+=1

#print(fences)
sides={}
for f in fences:
    sides[fences[f]]=0
#print(sides)
for y in range(len(grid)):
    lastn=""
    lasts=""
    for x in range(len(grid[0])):
        #calc n and s sides
        north=str(x)+"."+str(y)+"."+"n"
        south=str(x)+"."+str(y)+"."+"s"
        if north in fences:
            if fences[north]!=lastn:
                sides[fences[north]]+=1
#            print(x,y,fences[north],lastn,sides[fences[north]])
            lastn=fences[north]
        else:
            lastn=""
        if south in fences:
            if fences[south]!=lasts:
                sides[fences[south]]+=1
#            print(x,y,fences[south],lasts,sides[fences[south]])
            lasts=fences[south]
        else:
            lasts=""

for x in range(len(grid[0])):
    laste=""
    lastw=""
    for y in range(len(grid)):
        west=str(x)+"."+str(y)+"."+"w"
        east=str(x)+"."+str(y)+"."+"e"
        if west in fences:
 #           print(x,y,fences[west])
            if fences[west]!=lastw:
                sides[fences[west]]+=1
 #           print(x,y,fences[west],lastw,sides[fences[west]])
            lastw=fences[west]
        else:
            lastw=""
        if east in fences:
 #           print(x,y,fences[east])
            if fences[east]!=laste:
                sides[fences[east]]+=1
 #           print(x,y,fences[east],laste,sides[fences[east]])
            laste=fences[east]
        else:
            laste=""

totalf=0
totals=0
for k,f in fields.items():
    totalf+=f.adj*f.area
    totals+=sides[k]*f.area
#    print(f,f.adj,f.area,sides[k],"total fence cost:",f.adj*f.area,"total sides cost:",sides[k]*f.area)

print ("Fence based Cost:",totalf)
print ("sides based Cosr:",totals)
