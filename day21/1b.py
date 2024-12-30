# Reimplement as graphs for keypad and dirpad, calculate all shortest paths between each node and use those to build a set of paths, then take the shortest from final set as result
import sys
import networkx as nx
import functools

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

# I think I need to resolve the directions at this point, and suffix the A button at the end, I think this is easier than trying to retrofit
def getkeypaths(a,b,paths):
    temp=set()
    if len(paths)>0:
        for path in paths:
            for p in keypaths[a][b]:
                s=""
                for i in range(len(p)-1):
                    u=p[i]
                    v=p[i+1]
                    s+=keys[u][v]['d']
                temp.add(path+s+"A")
    else:
        for p in keypaths[a][b]:
            s=""
            for i in range(len(p)-1):
                u=p[i]
                v=p[i+1]
                s+=keys[u][v]['d']
            temp.add(s+"A")
    return temp

def getdirpaths(a,b,paths):
    temp=set()
    if len(paths)>0:
        for path in paths:
            for p in dirpaths[a][b]:
                s=""
                for i in range(len(p)-1):
                    u=p[i]
                    v=p[i+1]
                    s+=dirs[u][v]['d']
                temp.add(path+s+"A")
    else:
        for p in dirpaths[a][b]:
            s=""
            for i in range(len(p)-1):
                u=p[i]
                v=p[i+1]
                s+=dirs[u][v]['d']
            temp.add(s+"A")
    return temp


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

lengths={}
total=0
for code in codes:
    code="A"+code
    lengths[code]=10000
    paths=set()
    for i in range(len(code)-1):
#        print(code[i],code[i+1])
        paths=getkeypaths(str(code[i]),str(code[i+1]),paths)
    print(code)
#    for p in paths:
#        print(p)

#robot stage 1
    for path in paths:
        path="A"+path
        dirs1=set()
        for i in range(len(path)-1):
#            print(path[i],path[i+1])
            dirs1=getdirpaths(str(path[i]),str(path[i+1]),dirs1)
#        print(path)
#        for p in dirs1:
#            print(p)

#robot stage 2
        for path2 in dirs1:
            path2="A"+path2
            dirs2=set()
            for i in range(len(path2)-1):
#                print(path[i],path[i+1])
                dirs2=getdirpaths(str(path2[i]),str(path2[i+1]),dirs2)
#            print(path)
            print(len(min(dirs2, key=len)), min(dirs2, key=len))
            if len(min(dirs2, key=len))<lengths[code]:
                lengths[code]=len(min(dirs2, key=len))

for k,v in lengths.items():
    total=total+(int(k[1:-1])*v)
print(lengths)
print(total)
