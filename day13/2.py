import sys
import re
import math
from sympy import Eq, solve
from sympy.abc import a,b


class game:
    def __init__(self,ax,ay,bx,by,px,py):
        self.ax=int(ax)
        self.ay=int(ay)
        self.bx=int(bx)
        self.by=int(by)
        self.px=int(px)
        self.py=int(py)
        self.py2=int(py)+10000000000000
        self.px2=int(px)+10000000000000

filename="input.txt"
if len(sys.argv)>1:
    filename=sys.argv[1]

f = open(filename)

acost=3
bcost=1

games=[]
for line in f.readlines():
    match=re.match("Button A: X\+(\d+), Y\+(\d+)",line)
    if match:
        ax=match.group(1)
        ay=match.group(2)
#        print ("Button A",ax,ay)
    match=re.match("Button B: X\+(\d+), Y\+(\d+)",line)
    if match:
        bx=match.group(1)
        by=match.group(2)
#        print ("Button B",bx,by)
    match=re.match("Prize: X=(\d+), Y=(\d+)",line)
    if match:
        px=match.group(1)
        py=match.group(2)
#        print ("target",px,py)
        games.append(game(ax,ay,bx,by,px,py))

#For each game, calculate a directed graph of costs until we've calculated at least (px/minimum of ax and bx) or (py/minimum of ay and by) - nodes whichever is larger
# first vertex is 0,0 each edge has weight of cost (A cost or B cost)
cost1=0
cost2=0
for g in games:
    #calculate whether it's solvable - we must have an integer number of A and B presses
    sol=solve([ Eq(g.ax*a+g.bx*b,g.px),Eq(g.ay*a+g.by*b,g.py)])
    if sol[a].is_integer and sol[b].is_integer:
        #we have a solution
        cost1+=(acost*sol[a]+bcost*sol[b])
    sol=solve([ Eq(g.ax*a+g.bx*b,g.px2),Eq(g.ay*a+g.by*b,g.py2)])
    if sol[a].is_integer and sol[b].is_integer:
        #we have a solution
        cost2+=(acost*sol[a]+bcost*sol[b])

print(cost1,cost2)
