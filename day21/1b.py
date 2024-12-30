# Reimplement as graphs for keypad and dirpad, calculate all shortest paths between each node and use those to build a set of paths, then take the shortest from final set as result
import sys
import networkx as nx

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

def mapkeypad(code):
    # start at A, avoid 0,3 (if xdif is neg, move y first, otherwise x first)
    # Need to press A after each key
    seq=""
    lastx=keymap['A'][0]
    lasty=keymap['A'][1]
    for key in code:
        nextx=keymap[key][0]
        nexty=keymap[key][1]
        xdif=lastx-nextx
        ydif=lasty-nexty
        if ydif<0:
            yc="v"
        else:
            yc="^"
        if xdif<0:
            xc=">"
            for i in range(abs(xdif),0,-1):
                seq+=xc
            for i in range(abs(ydif),0,-1):
                seq+=yc
        else:
            xc="<"
            for i in range(abs(ydif),0,-1):
                seq+=yc
            for i in range(abs(xdif),0,-1):
                seq+=xc
        lastx=nextx
        lasty=nexty
        seq+="A"
    return seq

def mapdirpad(code):
    # start at A, avoid 0,0 (if xdif is neg, move y first, otherwise x first)
    # Need to press A after each key
    seq=""
    lastx=dirmap['A'][0]
    lasty=dirmap['A'][1]
    for key in code:
        nextx=dirmap[key][0]
        nexty=dirmap[key][1]
        xdif=lastx-nextx
        ydif=lasty-nexty
        if ydif<0:
            yc="v"
        else:
            yc="^"
        if xdif<0:
            xc=">"
            for i in range(abs(xdif),0,-1):
                seq+=xc
            for i in range(abs(ydif),0,-1):
                seq+=yc
        else:
            xc="<"
            for i in range(abs(ydif),0,-1):
                seq+=yc
            for i in range(abs(xdif),0,-1):
                seq+=xc
        lastx=nextx
        lasty=nexty
        seq+="A"
    return seq


keys=nx.Graph()
dirs=nx.Graph()
keys.add_edges_from([("A",0),("A",3),(0,2),(3,2),(3,6),(2,5),(2,1),(1,4),(4,7),(5,8),(5,6),(6,9),(9,8),(8,7),(4,5)])
dirs.add_edges_from([("A","^"),("A",">"),("^","v"),(">","v"),("v","<")])

keymap={'0':[1,3],'A': [2,3],'1':[0,2],'2':[1,2],'3':[2,2],'4':[0,1],'5':[1,1],'6':[2,1],'7':[0,0],'8':[1,0],'9':[2,0]}
dirmap={'^':[1,0],'A':[2,0],'<':[0,1],'v':[1,1],'>':[2,1]}

codes=[]
for line in f.readlines():
    codes.append(line.strip())

total=0
for i in codes:
    print(i)
    seq=mapkeypad(i)
    print(seq)
    seq2=mapdirpad(seq)
    print(seq2)
    seq3=mapdirpad(seq2)
    print(seq3)
    cost=int(i[0:-1])
    print(len(seq3),cost)
    cost=cost*len(seq3)
    total+=cost
    print(cost)

print(total)

