# Next attempt, for each layer, build a graph to represent possible sequences to represent the previous layer sequences
# Then find all shortest paths for that layer, prune to that and use to build next layer graph?
# Maybe some caching of function results will be required too.

# Reimplement as graphs for keypad and dirpad, calculate all shortest paths between each node and use those to build a set of paths, then take the shortest from final set as result
import sys
import networkx as nx
import functools

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)
lmax=3

# I think I need to resolve the directions at this point, and suffix the A button at the end, I think this is easier than trying to retrofit

def buildlayer(g):
    ng=nx.DiGraph()
    ng.add_node("start")
    nn=0
    #for all shortest paths between left and right hand end of sequence:
    for path in nx.all_shortest_paths(g,"start","end")
        #for each node in this path:
        for node in path:
            # We are always computing travel from an A button press
            last="A"
            #Get the sequence represented by this node
            nodeseq=g[node]['seq']
            for c in nodeseq:
                paths=getdirpaths(last,c)
                if len(paths)>1:
                    for p in paths:


def getkeypaths2(path):
    temp=set()
    for i in range(len(path)-1):
        temp2=set()
        for p in keypaths[path[i]][path[i+1]]:
            s=""
            for j in range(len(p)-1):
                u=p[j]
                v=p[j+1]
                s+=keys[u][v]['d']
            if len(temp)>0:
                for tp in temp:
                    temp2.add(tp+s+"A")
            else:
                temp2.add(s+"A")
        temp=temp2
    return temp

def getdirpaths(a,b,layer,index):
    #have we calculcated from this layer and this pair of keys before?
    print("dirpath computing",a,b,"at layer",layer,"index",index)
    if a+b+str(layer)+str(index) in pathcache:
        print("cache hit",a,b,layer,index,"returning with value",pathcache[a+b+str(layer)+str(index)])
        return pathcache[a+b+str(layer)+str(index)]
    #No, carry on with calculation
    length={}
    temp=set()
    #for every permutation of paths between a and b
    for p in dirpaths[a][b]:
        if index==0:
            print(p,"at left extreme, prepending with A for next layer")
            s="A"
        else:
            s=""
        # replace each pair of keys with the direction needed to be pressed to make that move
        for j in range(len(p)-1):
            u=p[j]
            v=p[j+1]
            s+=dirs[u][v]['d']
        #Check this logic, we need to think about when we need to press A, and how to start at A at each new layer. I used to prepend the next layer but with DFS this won't work, I need to keep track of the lefthand side of the tree I think, and prefix with A if it's the far left character at each layer?
        s+="A"
        temp.add(s)
    print("built",len(temp),"dirpath paths for",a,b,"at layer",layer,"paths are",temp)
    if layer==lmax:
        shortest=1000000000
        for seq in temp:
            if len(seq)<shortest:
                if index==0:
                    shortest=len(seq)-1
                else:
                    shortest=len(seq)
        print("bottomed out at layer",lmax,"calculating shortest sequence is",shortest)
        return shortest
    else:
        for seq in temp:
            if seq=="A":
                length[seq]=1
            else:
                length[seq]=0
            for i in range(len(seq)-1):
                length[seq]+=getdirpaths(seq[i],seq[i+1],layer+1,index+i)
    minlength=min(length.values())
    print("values for paths from here were ",length.values())
    print("adding to cache",a,b,"layer",layer,"position",index,"value",minlength)
    pathcache[a+b+str(layer)+str(index)]=minlength
    return minlength



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
    lengths[code]=999999999999999
    #initialise an empty set to store all unique permutations
    paths=set()
    #for each pair of keys in code
    r=getkeypaths2(code)
    paths.update(r)
    print("running DFS on ",code)
    for path in paths:
        print("trying possible path for",code,path)
        length=0
        path="A"+path
        for i in range(len(path)-1):
            length+=getdirpaths(path[i],path[i+1],1,i)
        print("length for path",path,"is",length)
        if length<lengths[code]:
            lengths[code]=length
for k,v in lengths.items():
    total=total+(int(k[1:-1])*v)
print(lengths)
print(total)
