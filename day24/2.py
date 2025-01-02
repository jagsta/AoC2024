import sys
import re

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f = open(file)

values={}
commands=[]
for line in f.readlines():
    match=re.match(r'(\w\d\d): (\d)',line)
    if match:
        values[match.group(1)]=int(match.group(2))
    else:
        match=re.match(r'(\w+\d*) (\w+) (\w+\d*) -> (\w+\d*)',line)
        if match:
            if match.group(1) not in values:
                values[match.group(1)]=None
            if match.group(3) not in values:
                values[match.group(3)]=None
            if match.group(4) not in values:
                values[match.group(4)]=None
            commands.append({"in1":match.group(1),"in2":match.group(3),"cmd":match.group(2),"out":match.group(4),"visited":False})
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
