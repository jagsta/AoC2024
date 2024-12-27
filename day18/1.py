import sys
import networkx as nx

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

i=0
while i<limit:
    line=f.readline().strip()
    coords = line.split(",")
    grid[int(coords[1])][int(coords[0])]="#"
    i+=1


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
