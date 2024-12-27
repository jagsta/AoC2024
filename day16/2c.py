# Dijkstra is surely the way to go here, using a minheap to keep all untravelled nodes
# Need to understand how to account for turns on path

#First attempt - some dude has written a modified dijkstra implementation which can calculate with turn penalties

# Dijkstra
# min heap
# Start at source
# for all adjacent nodes, calculate cost to reach them, compare to stored cost, if lower or equal,  store the new cost
# Add source to visited, add adjacents to min heap
# Take lowest from min heap and repeat until source node is target
from heapq import heappush, heappop
import sys

sdirs=[[0,-1,"n"],[1,0,"e"],[0,1,"s"],[-1,0,"w"]]

filename="input.txt"
if len(sys.argv)>1:
    filename=sys.argv[1]

f = open(filename)

minheap=[]
grid=[]
graph={}
target=""
source=""
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

#Now add adjacencies and weights
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x]!="#":
            graph[str(x)+"."+str(y)]={}
            #Check for adjacencies
            adj=[]
            for d in sdirs:
                if grid[y+d[1]][x+d[0]]!="#":
                    adj.append([x+d[0],y+d[1]])
                    if len(adj)==2:
                        if adj[0][0]-adj[1][0]==0 or adj[0][1]-adj[1][1]==0:
                            if str(adj[0][0])+"."+str(adj[0][1]) in graph[str(x)+"."+str(y)]:
                                if graph[str(x)+"."+str(y)][str(adj[0][0])+"."+str(adj[0][1])]<=1:
                                    graph[str(x)+"."+str(y)][str(adj[0][0])+"."+str(adj[0][1])]=1
                            if str(adj[1][0])+"."+str(adj[1][1]) in graph[str(x)+"."+str(y)]:
                                if graph[str(x)+"."+str(y)][str(adj[1][0])+"."+str(adj[1][1])]<=1:
                                    graph[str(x)+"."+str(y)][str(adj[1][0])+"."+str(adj[1][1])]=1
                            if str(adj[0][0])+"."+str(adj[0][1]) not in graph:
                                graph[str(adj[0][0])+"."+str(adj[0][1])]={}
                            if str(x)+"."+str(y) in graph[str(adj[0][0])+"."+str(adj[0][1])]:
                                if graph[str(adj[0][0])+"."+str(adj[0][1])][str(x)+"."+str(y)]<=1:
                                    graph[str(adj[0][0])+"."+str(adj[0][1])][str(x)+"."+str(y)]=1
                            if str(adj[1][0])+"."+str(adj[1][1]) not in graph:
                                graph[str(adj[1][0])+"."+str(adj[1][1])]={}
                            if str(x)+"."+str(y) in graph[str(adj[1][0])+"."+str(adj[1][1])]:
                                if graph[str(adj[1][0])+"."+str(adj[1][1])][str(x)+"."+str(y)]<=1:
                                    graph[str(adj[1][0])+"."+str(adj[1][1])][str(x)+"."+str(y)]=1
                        else:
                            graph[str(x)+"."+str(y)][str(adj[0][0])+"."+str(adj[0][1])]=501
                            graph[str(x)+"."+str(y)][str(adj[1][0])+"."+str(adj[1][1])]=501
                            if str(adj[0][0])+"."+str(adj[0][1]) not in graph:
                                graph[str(adj[0][0])+"."+str(adj[0][1])]={}
                            graph[str(adj[0][0])+"."+str(adj[0][1])][str(x)+"."+str(y)]=501
                            if str(adj[1][0])+"."+str(adj[1][1]) not in graph:
                                graph[str(adj[1][0])+"."+str(adj[1][1])]={}
                            graph[str(adj[1][0])+"."+str(adj[1][1])][str(x)+"."+str(y)]=501
                    if len(adj)>2:
                        graph[str(x)+"."+str(y)]["zz"]=1
                        for ai,a in enumerate(adj):
                            for b in adj[ai+1:]:
                                if a[0] - b[0]==0 or a[1]-b[1]==0:
                                    if str(a[0])+"."+str(a[1]) not in graph:
                                        graph[str(a[0])+"."+str(a[1])]={}
                                    graph[str(a[0])+"."+str(a[1])][str(b[0])+"."+str(b[1])]=2
                                    if str(b[0])+"."+str(b[1]) not in graph:
                                        graph[str(b[0])+"."+str(b[1])]={}
                                    graph[str(b[0])+"."+str(b[1])][str(a[0])+"."+str(a[1])]=2
                                else:
                                    if str(a[0])+"."+str(a[1]) not in graph:
                                        graph[str(a[0])+"."+str(a[1])]={}
                                    graph[str(a[0])+"."+str(a[1])][str(b[0])+"."+str(b[1])]=1002
                                    if str(x)+"."+str(y) in graph[str(a[0])+"."+str(a[1])]:
                                        del graph[str(a[0])+"."+str(a[1])][str(x)+"."+str(y)]
                                    if str(b[0])+"."+str(b[1]) not in graph:
                                        graph[str(b[0])+"."+str(b[1])]={}
                                    graph[str(b[0])+"."+str(b[1])][str(a[0])+"."+str(a[1])]=1002
                                    if str(x)+"."+str(y) in graph[str(b[0])+"."+str(b[1])]:
                                        del graph[str(b[0])+"."+str(b[1])][str(x)+"."+str(y)]



for line in grid:
    l=""
    for c in line:
        l+=c
    print(l)

delq=set()
for i in graph:
    if "zz" in graph[i]:
        delq.add(i)

for i in delq:
    del graph[i]
print(graph)

print(graph[source])
print(graph[target])

#Add bearing for each edge
    #print(e[0],e[1])
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
