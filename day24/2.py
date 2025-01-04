import sys
import re

class gate:
    def __init__(self,in1,in2,out):
        self.inputs={in1,in2}
        self.out=out

    def __str__(self):
        return f'inputs:{self.inputs} out:{self.out}'

class half_adder:
    def __init__(self,gxor=None,gand=None):
        self.gxor=gxor
        self.gand=gand

    def outs(self):
        self.cout=self.gand.out
        self.out=self.gxor.out
        return [self.out,self.cout]

class full_adder:
    def __init__(self,bit,gxor1=None,gand1=None,gxor2=None,gand2=None,gor=None):
        self.bit=bit
        self.gxor1=gxor1
        self.gxor2=gxor2
        self.gand1=gand1
        self.gand2=gand2
        self.gor=gor

    def __str__(self):
        return f'bit:{self.bit} gxor1:{self.gxor1} gxor2:{self.gxor2} gand1:{self.gand1} gand2{self.gand2} gor{self.gor}'

    def outs(self):
        if self.gor:
            self.cout=self.gor.out
        else:
            self.cout=None
        if self.gxor2:
            self.out=self.gxor2.out
        else:
            self.out=None
        return [self.out,self.cout]

    def check(self,bit,adders):
        valid=True
        outs=set()
        if bit < 10:
            x="x0"+str(bit)
            y="y0"+str(bit)
            z="z0"+str(bit)
        else:
            x="x"+str(bit)
            y="y"+str(bit)
            z="z"+str(bit)
        #1. Are the two bit inputs correct?
        if x not in self.gxor1.inputs:
            valid=False
            outs.add(x)
        if y not in self.gxor1.inputs:
            valid=False
            outs.add(y)
        #2. Is the carry bit input correct?
        if self.gxor2 and (adders[bit-1].cout not in self.gxor2.inputs or adders[bit-1].cout not in self.gand2.inputs):
            valid = False
            outs.add(adders[bit-1].cout)
        #3. Is xor2 bit inputs correect?
        if self.gxor1 and self.gxor2 and self.gxor1.out not in self.gxor2.inputs:
            valid = False
            outs.add(self.gxor1.out)
        if self.gxor2 and adders[bit-1].cout  not in self.gxor2.inputs:
            valid = False
            outs.add(adders[bit-1].cout)
        #5. Is SUM output correct?
        if self.gxor2 and self.gxor2.out != z:
            valid = False
            outs.add(self.gxor2.out)
            outs.add(z)
        #6. Is and1 bit inputs correct?
        if x not in self.gand1.inputs:
            valid = False
            outs.add(x)
        if y not in self.gand1.inputs:
            valid = False
            outs.add(y)
        #7. Is and2 bit inputs correct?
        if self.gxor1 and self.gand2 and self.gxor1.out not in self.gand2.inputs:
            valid = False
            outs.add(self.gxor1.out)
        if self.gor and self.gand1.out not in self.gor.inputs:
            valid = False
            outs.add(self.gand1.out)
        if self.gor and self.gand2.out not in self.gor.inputs:
            valid = False
            outs.add(self.gand2.out)
        if not (self.gand1 and self.gand2 and self.gxor1 and self.gxor2 and self.gor):
            valid = False
            outs.add("missing logic component")
        return valid,outs


file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f = open(file)

adders=[None]*45
ors={}
ands={}
xors={}

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
            if match.group(2) == "OR":
                ors[match.group(1)+"."+match.group(3)]=gate(match.group(1),match.group(3),match.group(4))
            if match.group(2) == "AND":
                ands[match.group(1)+"."+match.group(3)]=gate(match.group(1),match.group(3),match.group(4))
            if match.group(2) == "XOR":
                xors[match.group(1)+"."+match.group(3)]=gate(match.group(1),match.group(3),match.group(4))

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

wires=set()
carry=""
for i in range(45):
    if i<10:
        x="x0"+str(i)
        y="y0"+str(i)
        z="z0"+str(i)
    else:
        x="x"+str(i)
        y="y"+str(i)
        z="z"+str(i)
    resxors = [key for key in xors.keys() if re.search(x, key)]
    resands = [key for key in ands.keys() if re.search(x, key)]
    if resxors[0] in xors and resands[0] in ands:
        print("found xor for",x)
        if i==0:
            adders[i]=half_adder(xors[resxors[0]],ands[resands[0]])
        else:
            adders[i]=full_adder(i,xors[resxors[0]],ands[resands[0]])
    else:
        print("missed x input:",x)
    xorout=xors[resxors[0]].out
    andout=ands[resands[0]].out
    if i==0:
        carry=andout
        adders[i].outs()
    else:
        and2in=adders[i-1].cout
        xor2in=adders[i-1].cout
        res = [key for key in xors.keys() if re.search(xorout, key)]
        if len(res)==1:
            adders[i].gxor2=xors[res[0]]
        elif len(res)>1:
            print("extra xor2 for adder",i)
        else:
            print("missed xor2 for adder",i)
            res = [key for key in xors.keys() if re.search(xor2in, key)]
            if len(res)==1:
                adders[i].gxor2=xors[res[0]]
            elif len(res)>1:
                print("extra xor2 for adder",i)
            else:
                print("missed xor2 for adder",i)
        res = [key for key in ands.keys() if re.search(xorout, key)]
        if len(res)==1:
            adders[i].gand2=ands[res[0]]
        elif len(res)>1:
            print("extra and2 for adder",i)
        else:
            print("missed and2 for adder",i)
            res = [key for key in ands.keys() if re.search(and2in, key)]
            if len(res)==1:
                adders[i].gand2=ands[res[0]]
            elif len(res)>1:
                print("extra and2 for adder",i)
            else:
                print("missed and2 for adder",i)
        res = [key for key in ors.keys() if re.search(andout, key)]
        if len(res)==1:
            adders[i].gor=ors[res[0]]
        elif len(res)>1:
            print("extra or for adder",i)
        else:
            print("missed or for adder",i)
            res = [key for key in ors.keys() if re.search(adders[i].gand2.out, key)]
            if len(res)==1:
                adders[i].gor=ors[res[0]]
            elif len(res)>1:
                print("extra or for adder",i)
            else:
                print("missed or for adder",i)
        adders[i].outs()
        validate,error=adders[i].check(i,adders)
        if not validate:
            wires.update(error)
            print("bit",i,"invalid",error)
            print(adders[i])
            print("bit",i-1,"cout",adders[i-1].cout)

s=""
for i in sorted(wires):
    s+=i+","
print(s[:-1])
