import copy
f = open("input.txt")

def move_guard(themap,x,y,direction):
    #print (themap[y][x],x,y,direction)
    if themap[y][x]=="X":
        visited=1
    else:
        visited=0
    nx=x
    ny=y
    if direction==0: ny-=1
    elif direction==1: nx+=1
    elif direction==2: ny+=1
    elif direction==3: nx-=1
    if nx<0 or ny<0 or nx>max_x or ny>max_y:
        #we've exited the map, replace guard with visited and end
        themap[y][x]="X"
        return x,y,direction,1,visited
    elif themap[ny][nx]=="#":
        #we're facing an obstruction, turn right
        direction+=1
        if direction>3: direction=0
    #    print("turn right, direction now:",direction)
        return x,y,direction,0,visited
    else:
        themap[y][x]="X"
    #    print("move, direction:",direction," new coords:",nx,ny)
        return nx,ny,direction,0,visited

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

loopmap= copy.deepcopy(guardmap)
max_x=len(guardmap[0])-1
max_y=y-1
loopx=guardx
loopy=guardy
loopdir=direction
print(direction,guardx,guardy,max_x,max_y)
while not exited:
    guardx, guardy, direction, exited, loopcount = move_guard(guardmap,guardx,guardy,direction)

for line in guardmap:
    for pixel in line:
        if pixel=="X": visited+=1

print("visited: ",visited)
cury=0
obstacles=0
for line in guardmap:
    curx=0
    for pixel in line:
        if pixel=="X":
            print("testing ",curx,cury)
            testmap=copy.deepcopy(loopmap)
            #print(testmap)
            testx=loopx
            testy=loopy
            testdir=loopdir
            #this is a potential spot for a new obstacle, test to see if it causes a loop
            testmap[cury][curx]="#"
            loopdetect=0
            exited=0
            while not exited and loopdetect>=0:
                testx,testy,testdir,exited,looping=move_guard(testmap,testx,testy,testdir)
                #print (testx,testy,testdir,exited,looping)
                if looping:
                    loopdetect-=1
                else:
                    loopdetect+=1
                #print(loopdetect)
            if loopdetect<0:
                obstacles+=1
        curx+=1
    cury+=1
print("potential obstacles:",obstacles)
