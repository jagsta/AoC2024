f = open("input.txt")

def move_guard(x,y,direction,exited):
    nx=x
    ny=y
    if direction==0: ny-=1
    elif direction==1: nx+=1
    elif direction==2: ny+=1
    elif direction==3: nx-=1
    if nx<0 or ny<0 or nx>max_x or ny>max_y:
        #we've exited the map, replace guard with visited and end
        guardmap[y][x]="X"
        return x,y,direction,1
    elif guardmap[ny][nx]=="#":
        #we're facing an obstruction, turn right
        direction+=1
        if direction>3: direction=0
        print("turn right, direction now:",direction)
        return x,y,direction,0
    else:
        guardmap[y][x]="X"
        print("move, direction:",direction," new coords:",nx,ny)
        return nx,ny,direction,0

guardmap=[]

direction=0 #0=N,1=E,2=S,3=W
visited=0
guardN="^"
guardE=">"
guardS="v"
guardW="<"
exited=0

guardx=0
guardy=0
y=0
for line in f.readlines():
    guardmap.append(list(line.strip()))
    if guardN in line:
        direction=0
        guardy=y
        guardx=line.index(guardN)
    elif guardE in line:
        direction=1
        guardy=y
        guardx=line.index(guardE)
    elif guardS in line:
        direction=2
        guardy=y
        guardx=line.index(guardS)
    elif guardW in line:
        direction=3
        guardy=y
        guardx=line.index(guardW)
    y+=1

max_x=len(guardmap[0])-1
max_y=y-1
print(direction,guardx,guardy,max_x,max_y)
while not exited:
    guardx, guardy, direction, exited = move_guard(guardx,guardy,direction,exited)

for line in guardmap:
    for pixel in line:
        if pixel=="X": visited+=1

print("visited: ",visited)
