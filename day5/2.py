import re
import networkx as nx
import matplotlib.pyplot as plt

f=open("input.txt")

v={}
inadj=[]
runs=[]
total=0

#Read in the input data, a dict of unique page numbers mapped to an index (vertices), an array of adjacency rules (edges) and an array of page orderings.
index=0
for line in f.readlines():
    vertices=re.match("(\d{2})\|(\d{2})",line)
    if vertices:
        inadj.append([int(vertices.group(1)),int(vertices.group(2))])
        if vertices.group(1) not in v:
            v[vertices.group(1)]=index
            index+=1
        if vertices.group(2) not in v:
            v[vertices.group(2)]=index
            index+=1
    elif line.strip():
        runs.append(line.strip().split(","))
print(v)

#Now we know how many vertices we need to graph, map adjacencies

numv=len(v)
graph = [[] for _ in range(numv)]

for i in inadj:
    graph[v[str(i[0])]].append(v[str(i[1])])
#print(len(v))
#print(v)
#print(graph)
#g = nx.DiGraph(inadj)
#if (nx.is_strongly_connected(g)): print ("strong connections")
#print(nx.find_cycle(g))
#h = nx.condensation(g)
#print(h.nodes.data())
#print(list(nx.topological_sort(h)))
#g.add_nodes_from(v.keys())
#for i in inadj:
#    print(i)
#    g.add_edge(str(i[0]),str(i[1]))

#print(list(nx.topological_sort(g)))

#nx.draw(g,with_labels=True)
#plt.draw()
#plt.show()


badpages=[]
for run in runs:
    last=''
    ok=1
    for page in run:
        if not last:
            last=page
        else:
            if not v[page] in graph[v[last]]:
 #               print ("bad: ",v[page]," not in: ",graph[v[last]])
                badpages.append(run)
                ok=0
                break
            else:
                last=page
    if (ok==1):
        mid=int((len(run)-1)/2)
        total+=int(run[mid])
 #       print("good, adding",int(run[mid]),"to total for: ",run)
print(total)

badtotal=0

for badpage in badpages:
    g = nx.DiGraph()
    #goodpage=[]
    for i in inadj:
        if str(i[0]) in badpage and str(i[1]) in badpage:
            g.add_edge(i[0],i[1])
#        print(graph[v[i]])
#        g.add_nodes_from(graph[v[i]])
    print(nx.is_strongly_connected(g))
    goodpage=(list(nx.topological_sort(g)))
    print(goodpage)
#    nx.draw(g,with_labels=True)
#    plt.draw()
#    plt.show()

    #sanity check
    last=''
    ok=1
    for page in goodpage:
         if not last:
             last=str(page)
         else:
             if not v[str(page)] in graph[v[last]]:
                 print ("bad: ",v[page]," not in: ",graph[v[last]])
                 ok=0
                 break
             else:
                 last=str(page)
    if (ok==1):
        mid=int((len(goodpage)-1)/2)
        badtotal+=int(goodpage[mid])
        print(badpage,"is now: ",goodpage," adding index ",mid," (",goodpage[mid],") to total:",badtotal)

print("bad pages total is: ",badtotal)
