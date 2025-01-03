import sys
import re
import networkx as nx

class gxor:
    def __init__(self,in1,in2,out):
        self.inputs=set(in1,in2)
        self.out=out

class gor:
    def __init__(self,in1,in2,out):
        self.inputs=set(in1,in2)
        self.out=out

class gand:
    def __init__(self,in1,in2,out):
        self.inputs=set(in1,in2)
        self.out=out

class half_adder:
    def __init__(self,gxor,gand):
        self.gxor=gxor
        self.gand=gand
        self.cout=self.gand.out
        self.out=self.gxor.out

class full_adder:
    def __init__(self,bit,gxor1,gxor2,gand1,gand2,gor):
        self.bit=bit
        self.gxor1=gxor1
        self.gxor2=gxor2
        self.gand1=gand1
        self.gand2=gand2
        self.gor=gor
        self.cout=self.gor.out
        self.out=self.gxor2.out

    def check(bit,adders):
        valid=True
        if bit < 10:
            x="x0"+str(bit)
            y="y0"+str(bit)
            z="z0"+str(bit)
        else:
            x="x"+str(bit)
            y="y"+str(bit)
            z="z"+str(bit)
        if x not in self.gxor1.inputs or y not in self.gxor1.inputs::
            valid = False
        if self.gxor1.out not in self.gxor2.inputs:
            valid = False
        if self.gxor2.out != z
            valid = False
        if x not in self.gand1.inputs or y not in self.gand1.inputs:
            valid = False
        if self.gxor1.out not in self.gand2.inputs:
            valid = False
        if self.gand1.out not in self.gor.inputs or self.gand2.out not in self.gor.inputs:
            valid = False
        if adders[bit-1].cout not in self.gxor2.inputs or adders[bit-1].cout not in self.gand2.inputs:
            valdi = False
        return valid


file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f = open(file)

G=nx.DiGraph()

values={}
commands=[]
for line in f.readlines():
    match=re.match(r'(\w\d\d): (\d)',line)
    if match:
        values[match.group(1)]=int(match.group(2))
        G.add_node(match.group(1))
    else:
        match=re.match(r'(\w+\d*) (\w+) (\w+\d*) -> (\w+\d*)',line)
        if match:
            if match.group(1) not in values:
                values[match.group(1)]=None
                G.add_node(match.group(1))
            if match.group(3) not in values:
                values[match.group(3)]=None
                G.add_node(match.group(3))
            if match.group(4) not in values:
                values[match.group(4)]=None
                G.add_node(match.group(4))
            commands.append({"in1":match.group(1),"in2":match.group(3),"cmd":match.group(2),"out":match.group(4),"visited":False})
            G.add_node(match.group(1)+"."+match.group(3),gate=match.group(2))
            G.add_edge(match.group(1),match.group(1)+"."+match.group(3))
            G.add_edge(match.group(3),match.group(1)+"."+match.group(3))
            G.add_edge(match.group(1)+"."+match.group(3),match.group(4))

#print(values)
#for c in commands:
#    print(c)
while None in values.values():
    for c in commands:
        if values[c["in1"]] is not None and values[c["in2"]] is not None and not c["visited"]:
            if c["cmd"]=="AND":
                values[c["out"]]=values[c["in1"]] & values[c["in2"]]
            if c["cmd"]=="OR":
                values[c["out"]]=values[c["in1"]] | values[c["in2"]]
            if c["cmd"]=="XOR":
                values[c["out"]]=values[c["in1"]] ^ values[c["in2"]]
            c["visited"]=True

bitlength=0
for k in values.keys():
    if k[0]=="z":
        bitlength+=1

result=[0]*bitlength

for k,v in values.items():
    if k[0] =="z":
        result[int(k[1:])]=v
        print(k,v)

answer=""
for b in reversed(result):
    answer+=str(b)
print(int(answer,2))



