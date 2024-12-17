import sys
import re
import matplotlib.pyplot as plt

class robot:
    def __init__(self,x,y,vx,vy):
        self.x=int(x)
        self.y=int(y)
        self.vx=int(vx)
        self.vy=int(vy)

filename="input.txt"
if len(sys.argv)>1:
    filename=sys.argv[1]

f=open(filename)

grid=[]

if filename=="input.txt":
    ymax=103
    xmax=101
else:
    ymax=7
    xmax=11

for y in range(ymax):
    grid.append([])
    for x in range(xmax):
        grid[y].append(0)

robots=[]

print(grid)

for line in f.readlines():
    match=re.match("p=(\d+),(\d+) v=(-*\d+),(-*\d+)",line)
    if match:
        print(match.group(1),match.group(2),match.group(3),match.group(4))
        robots.append(robot(match.group(1),match.group(2),match.group(3),match.group(4)))

cycles=100000
for i in range(cycles):
    pointsx=[]
    pointsy=[]
    for r in robots:
        nx = (r.x + r.vx)
        ny = (r.y + r.vy)
        if nx < 0:
            nx=nx+xmax
        if nx > xmax-1:
            nx=nx-xmax
        if ny < 0:
            ny=ny+ymax
        if ny > ymax-1:
            ny=ny-ymax
        r.x = nx
        r.y = ny
        pointsx.append(r.x)
        pointsy.append(r.y)
    if(i+1-48)%101==0:
        plt.scatter(pointsx,pointsy)
        plt.xlabel(i+1)
        plt.show()
    print (r.vx,r.vy,nx,ny)

qx = (xmax+1)/2-1
qy = (ymax+1)/2-1
print (qx,qy)

q1=0 #<qx and <qy
q2=0 #>qx and <qy
q3=0 #<qx and >ay
q4=0 #>qx and <ay

for r in robots:
    if r.y < qy:
        if r.x < qx:
            q1+=1
        elif r.x > qx:
            q2+=1
    elif r.y > qy:
        if r.x < qx:
            q3+=1
        if r.x > qx:
            q4+=1

print (q1,q2,q3,q4,(q1*q2*q3*q4))
