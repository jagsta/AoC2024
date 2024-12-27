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
#        if c==".":
            #Add a node
#            G.add_node(str(x)+c+str(y),x=x,y=y,weight=1)
        if c=="E":
            #Add target node
            target=str(x)+"."+str(y)
#            G.add_node(target,x=x,y=y,weight=1)
        if c=="S":
            #Add source node
            source=str(x)+"."+str(y)
#            dummy=str(x-1)+"."+str(y)
#            G.add_node(dummy,x=x-1,y=y,weight=0)
#            G.add_node(source,x=x,y=y,weight=1)
        x+=1
    y+=1
visited=set()
#Now add edges
nodemap={}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x]!="#":
            #Check for adjacencies
            adj=[]
            for d in sdirs:
                if grid[y+d[1]][x+d[0]]!="#":
                    adj.append([x+d[0],y+d[1]])
            if len(adj)==2:
                visited.add(str(x)+"."+str(y))
                for ai,a in enumerate(adj):
                    for b in (adj[ai+1:]):
                        if a[0]-b[0]==0 or a[1]-b[1]==0:
                            w=1
                        else:
                            w=501
                        #adj squares are hor or ver aligned, no turn, no additional nodes
                        if str(a[0])+"."+str(a[1]) not in visited or (G.has_edge(str(a[0])+"."+str(a[1]),str(x)+"."+str(y)) and G.edges[str(a[0])+"."+str(a[1]),str(x)+"."+str(y)]["weight"]<=1):
                            G.add_edge(str(x)+"."+str(y),str(a[0])+"."+str(a[1]),weight=w)
                        if str(b[0])+"."+str(b[1]) not in visited or (G.has_edge(str(b[0])+"."+str(b[1]),str(x)+"."+str(y)) and G.edges[str(b[0])+"."+str(b[1]),str(x)+"."+str(y)]["weight"]<=1):
                            G.add_edge(str(x)+"."+str(y),str(b[0])+"."+str(b[1]),weight=w)
            if len(adj)>2:
                visited.add(str(x)+"."+str(y))
                G.add_node(str(x)+"."+str(y),delete=1)
                for ai,a in enumerate(adj):
                    for b in (adj[ai+1:]):
                        if a[0]-b[0]==0 or a[1]-b[1]==0:
                            w=2
                        else:
                            w=1002
                        G.add_edge(str(a[0])+"."+str(a[1]),str(b[0])+"."+str(b[1]),weight=w)
                        #adj squares are hor or ver aligned, no turn, no additional nodes

deleted=set()
for i in list(G.nodes.data('delete')):
    if i[1]==1:
        deleted.add(i[0])
        G.remove_node(i[0])
for i,line in enumerate(grid):
    l=""
    for c in line:
        l+=c
    print(l)

print(list(G.nodes))
#Add bearing for each edge
print(list(G.edges(data=True)))

pred={}
dist={}
pred,dist=nx.dijkstra_predecessor_and_distance(G, source, weight="weight")
#print([p for p in nx.all_shortest_paths(G, source=source, target=target)])
print("preds")
for p in pred:
    print(p,pred[p])

travelled=set()


def walk(node,pre):
    print("travelling",node)
    nxy=node.split(".")
    pxy=pre.split(".")
    nx=int(nxy[0])
    ny=int(nxy[1])
    px=int(pxy[0])
    py=int(pxy[1])
    if (abs(nx-px)==1 and abs(ny-py)==1):
    #or abs(nx-px)>1 or abs(ny-py)>1:
        if grid[py][nx]!="#":
            travelled.add(str(nx)+"."+str(py))
        if grid[ny][px]!="#":
            travelled.add(str(px)+"."+str(ny))
    if abs(nx-px)>1 or abs(ny-py)>1:
            print("skipped straight",nx,ny,px,py)
            travelled.add(str(int((nx+px)/2))+"."+str(int((ny+py)/2)))
            print("adding",(nx+px)/2,(ny+py)/2)
    travelled.add(node)
    if node == source:
        return
    for n in pred[node]:
        walk(n,node)
travelled.add(target)
for n in pred[target]:
    walk(n,target)
for y,_ in enumerate(grid):
    line=""
    for x,c in enumerate(grid[y]):
        if str(x)+"."+str(y) in travelled:
            line+="O"
        else:
            line+=c
    print(line)

print(len(travelled))
#print(path)
#path.insert(0,dummy)
#cost=0
#for i in range(len(path)-2):
#    if (path[i], path[i+1], path[i+2]) in p:
#        cost+=1001
#        print("penalty",path[i], path[i+1], path[i+2],cost)
#    else:
#        cost+=1
#        print(path[i], path[i+1], path[i+2],cost)
#
#print(cost)
#
