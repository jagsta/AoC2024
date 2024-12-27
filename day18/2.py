import sys
import networkx as nx

def testpath(n):
    grid= [["." for x in range(gridmax+1)] for y in range(gridmax+1)]
    G=nx.Graph()

    for i in range(n):
        grid[int(drops[i][1])][int(drops[i][0])]="#"
    for y,j in enumerate(grid):
        for x,i in enumerate(grid[y]):
            for d in sdirs:
                if x+d[0]>=0 and x+d[0]<=gridmax and y+d[1]>=0 and y+d[1]<=gridmax and grid[y][x]!="#":
                    if grid[y+d[1]][x+d[0]]!="#":
#                    print("adding at",d[2],x,y,x+d[0],y+d[1],grid[y+d[1]][x+d[0]])
                        G.add_edge(str(x)+"."+str(y),str(x+d[0])+"."+str(y+d[1]))

#    print(G.nodes)
#    print(G.edges)
    path=nx.shortest_path(G, source="0.0", target=str(gridmax)+"."+str(gridmax))
    print(n,len(path))
    return path

sdirs=[[0,-1,"n"],[1,0,"e"],[0,1,"s"],[-1,0,"w"]]

file="input.txt"
gridmax=70
limit=1024

if len(sys.argv)>1:
    file=sys.argv[1]
    gridmax=6
    limit=12

f=open(file)

grid= [["." for x in range(gridmax+1)] for y in range(gridmax+1)]

drops=[]
for line in f.readlines():
    l=line.strip()
    coords = l.split(",")
    drops.append([coords[0],coords[1]])
for i in range(1024):
    grid[int(drops[i][1])][int(drops[i][0])]="#"


for line in grid:
    s=""
    for c in line:
        s+=c
    print(s)

G=nx.Graph()

for y,j in enumerate(grid):
    for x,i in enumerate(grid[y]):
        for d in sdirs:
            if x+d[0]>=0 and x+d[0]<=gridmax and y+d[1]>=0 and y+d[1]<=gridmax and grid[y][x]!="#":
                if grid[y+d[1]][x+d[0]]!="#":
#                    print("adding at",d[2],x,y,x+d[0],y+d[1],grid[y+d[1]][x+d[0]])
                    G.add_edge(str(x)+"."+str(y),str(x+d[0])+"."+str(y+d[1]))

print(G.nodes)
print(G.edges)
path=nx.shortest_path(G, source="0.0", target=str(gridmax)+"."+str(gridmax))
print(path)
print(len(path)-1)
for i in range(len(drops)):
    p=testpath(i)
    if len(p)==0:
        break
