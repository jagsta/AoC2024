import sys
import networkx as nx

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

G=nx.Graph()
for line in f.readlines():
    pcs=line.strip().split("-")
    G.add_edge(pcs[0],pcs[1])

cycles=nx.simple_cycles(G,length_bound=3)

total=0
for i in list(cycles):
    tt=0
    for n in i:
        if n[0]=="t":
            tt=1
    total+=tt
print("total",total)
