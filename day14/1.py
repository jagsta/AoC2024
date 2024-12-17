import sys
import re

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

cycles=100
for r in robots:
    dx = r.vx * cycles
    dy = r.vy * cycles
    nx = (r.x + dx) % xmax
    ny = (r.y + dy) % ymax
    r.x = nx
    r.y = ny
    print (r.vx,r.vy,dx,dy,nx,ny)

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
