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
cliques=nx.find_cliques(G)

scliques=sorted(list(cliques), key=len)
biggest=scliques[-1]
secret=""
for i in sorted(biggest):
    secret+=i+","

print(biggest)
print(secret[:-1])

