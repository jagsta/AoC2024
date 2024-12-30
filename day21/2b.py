# Reimplement as graphs for keypad and dirpad, calculate all shortest paths between each node and use those to build a set of paths, then take the shortest from final set as result
import sys
import networkx as nx

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

# I think I need to resolve the directions at this point, and suffix the A button at the end, I think this is easier than trying to retrofit
def getkeypaths(a,b):
    temp=set()
    for p in keypaths[a][b]:
        s=""
        for i in range(len(p)-1):
            u=p[i]
            v=p[i+1]
            s+=keys[u][v]['d']
        temp.add(s+"A")
    return temp

def getdirpaths(a,b):
    temp=set()
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

pathcache={}

codes=[]
for line in f.readlines():
    codes.append(line.strip())

lengths={}
total=0
#for each code in our list
for code in codes:
    #prefix with starting position "A"
    code="A"+code
    #set a large length as the best for this code
    lengths[code]=10000000
    #initialise an empty set to store all unique permutations
    paths=set()
    #for each pair of keys in code
    for i in range(len(code)-1):
#        print(code[i],code[i+1])
        # get paths between these two keys
        if len(paths)>0:
            temp=set()
            for p in paths:
                r=getkeypaths(str(code[i]),str(code[i+1]))
                for rp in r:
                    print(r,rp,p)
                    temp.add(p+rp)
            paths=temp
        else:
            r=getkeypaths(str(code[i]),str(code[i+1]))
            paths.update(r)
    print(code)
    for p in paths:
        print(p)
    #Repeat this for however many layers of panels required
    imax=25
    for iterations in range(imax):
        print("Iteration",iterations)
        #
        #copy paths to a a new set to avoid in loop changes to set we iterate
        #for each path in our list
        tt=set()
        for path in paths:
            if path in pathcache:
                tt.update(pathcache[path])
                continue
            t=set()
            # start at A
            path="A"+path
            print(path)
            # iterate through the characters in the path
            for i in range(len(path)-1):
                # if this is the first time, paths will be empty
                if len(t)>0:
                    #We've started bulding new sequences
                    temp=set()
                    for p in t:
                        # Add to existing paths any permutations of routes from a to b
                        if str(path[i])+"."+str(path[i+1]) in pathcache:
                            #print("cache hit",str(path[i])+"."+str(path[i+1])+"."+p,pathcache[str(path[i])+"."+str(path[i+1])+"."+p])
                            for rp in pathcache[str(path[i])+"."+str(path[i+1])]:
                                temp.add(p+rp)
                            continue
                        r=getdirpaths(str(path[i]),str(path[i+1]))
                        pathcache[str(path[i])+"."+str(path[i+1])]=r
                        for rp in r:
                            temp.add(p+rp)
                    t=temp
                else:
                    if str(path[i])+"."+str(path[i+1]) in pathcache:
                        #print("cache hit",str(path[i])+"."+str(path[i+1]),pathcache[str(path[i])+"."+str(path[i+1])])
                        t.update(pathcache[str(path[i])+"."+str(path[i+1])])
                        continue
                    r=getdirpaths(str(path[i]),str(path[i+1]))
                    pathcache[str(path[i])+"."+str(path[i+1])]=r
                    t.update(r)
            tt.update(t)
            pathcache[path[1:]]=t
        paths=tt
        if iterations==imax-1:
            print(len(min(paths, key=len)), min(paths, key=len))
            if len(min(paths, key=len))<lengths[code]:
                lengths[code]=len(min(paths, key=len))

for k,v in lengths.items():
    total=total+(int(k[1:-1])*v)
print(lengths)
print(total)
