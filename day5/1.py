import re

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
print(graph)

for run in runs:
    last=''
    ok=1
    for page in run:
        if not last:
            last=page
        else:
            if not v[page] in graph[v[last]]:
 #               print ("bad: ",v[page]," not in: ",graph[v[last]])
                ok=0
                break
            else:
                last=page
    if (ok==1):
        mid=int((len(run)-1)/2)
        total+=int(run[mid])
#        print("good, adding",int(run[mid]),"to total for: ",run)
print(total)
