# Reimplement as graphs for keypad and dirpad, calculate all shortest paths between each node and use those to build a set of paths, then take the shortest from final set as result
import sys
import networkx as nx

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

def getkeypaths(a,b,paths):
    if len(paths)>0:
        for path in paths:
            for p in keypaths[a][b]:
                paths.add(path.append(p))
    else:
        for p in keypaths[a][b]:
            paths.add(p)
    return paths


#Build graphs of keypads, directional so we can capture the directional moves between keys, then compute all shortest paths for all pairs of keys and store in a dict of dicts
keys=nx.DiGraph()
dirs=nx.DiGraph()
#up
keys.add_edges_from([("A","3"),("0","2"),("3","6"),("2","5"),("1","4"),("4","7"),("5","8"),("6","9")], d="^")
dirs.add_edges_from([(">","A"),("v","^")], d="^")
#down
keys.add_edges_from([("7","4"),("8","5"),("9","6"),("4","1"),("5","2"),("6","3"),("2","0"),("3","A")], d="v")
dirs.add_edges_from([("A",">"),("^","v")], d="v")
#left
keys.add_edges_from([("A","0",),("3","2"),("2","1"),("6","5"),("9","8"),("8","7"),("5","4")], d="<")
dirs.add_edges_from([("A","^"),(">","v"),("v","<")], d="<")
#right
keys.add_edges_from([("0","A"),("2","3"),("1","2"),("5","6"),("8","9"),("7","8"),("4","5")], d=">")
dirs.add_edges_from([("^","A"),("v",">"),("<","v")], d=">")

keypaths=dict(nx.all_pairs_all_shortest_paths(keys))
dirpaths=dict(nx.all_pairs_all_shortest_paths(dirs))

for k,v in keypaths.items():
    print(k,v)
for k,v in dirpaths.items():
    print(k,v)

#print(keypaths["A"][7])

codes=[]
for line in f.readlines():
    codes.append(line.strip())

total=0
for code in codes:
    paths=set()
    #for each key pair, return all paths, then recurse for each each of those until end of code
    for i in range(len(code)-1):
        print(code[i],code[i+1])
        paths=getkeypaths(code[i],code[i+1],paths)
    print(code)
    for p in paths:
        print(p)

print(total)

