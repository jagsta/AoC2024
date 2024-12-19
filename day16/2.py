# Dijkstra is surely the way to go here, using a minheap to keep all untravelled nodes
# Need to understand how to account for turns on path

#First attempt - some dude has written a modified dijkstra implementation which can calculate with turn penalties
import networkx as nx
from shortest_path_util import *
from shortest_path_turn_penalty import shortest_path_turn_penalty
import sys

sdirs=[[0,-1,"n"],[1,0,"e"],[0,1,"s"],[-1,0,"w"]]

filename="input.txt"
if len(sys.argv)>1:
    filename=sys.argv[1]

f = open(filename)

grid=[]
G=nx.Graph()
target=""
source=""
dummy=""
y=0
for line in f.readlines():
    grid.append([])
    x=0
    for c in line.strip():
        print(c,x,y)
        grid[y].append(c)
        if c==".":
            #Add a node
            G.add_node(str(x)+c+str(y),x=x,y=y,weight=1)
        if c=="E":
            #Add target node
            target=str(x)+"."+str(y)
            G.add_node(target,x=x,y=y,weight=1)
        if c=="S":
            #Add source node
            source=str(x)+"."+str(y)
            dummy=str(x-1)+"."+str(y)
            G.add_node(dummy,x=x-1,y=y,weight=0)
            G.add_node(source,x=x,y=y,weight=1)
        x+=1
    y+=1

#Now add edges
G.add_edge(dummy,source)
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x]!="#":
            #Check for adjacencies
            for d in sdirs:
                if grid[y+d[1]][x+d[0]]!="#":
                    G.add_edge(str(x)+"."+str(y),str(x+d[0])+"."+str(y+d[1]))

for line in grid:
    l=""
    for c in line:
        l+=c
    print(l)

print(list(G.nodes))
#Add bearing for each edge
for e in G.edges:
    #print(e[0],e[1])
    bearing=calculate_bearing(G,e[0],e[1])
    G.edges[e[0],e[1]]["bearing"]=bearing
#    print(e[0],e[1],bearing)
print(list(G.edges(data=True)))

p = penalty_turns(G)
print(p)

path=shortest_path_turn_penalty(G, source, target, weight="weight",penalty=p, next_node=None)
print(path)
path.insert(0,dummy)
cost=0
for i in range(len(path)-2):
    if (path[i], path[i+1], path[i+2]) in p:
        cost+=1001
        print("penalty",path[i], path[i+1], path[i+2],cost)
    else:
        cost+=1
        print(path[i], path[i+1], path[i+2],cost)

print(cost)

