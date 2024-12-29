import sys

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

def mapkeypad(code):
    # start at A, avoid 0,0 (if xdif is neg, move y first, otherwise x first)
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
        elif ydif>0:
            yc="^"
        else:
            yc=""
        if xdif<0:
            xc=">"
            for i in range(abs(ydif),0,-1):
                seq+=yc
            for i in range(abs(xdif),0,-1):
                seq+=xc
        elif xdif>0:
            xc="<"
            for i in range(abs(xdif),0,-1):
                seq+=xc
            for i in range(abs(ydif),0,-1):
                seq+=yc
        else:
            for i in range(abs(ydif),0,-1):
                seq+=yc
        lastx=nextx
        lasty=nexty
        seq+="A"
    return seq

keymap={'0':[1,3],'A': [2,3],'1':[0,2],'2':[1,2],'3':[2,2],'4':[0,1],'5':[1,1],'6':[2,1],'7':[0,0],'8':[1,0],'9':[2,0]}
dirmap={'^':[1,0],'A':[2,0],'<':[0,1],'v':[1,1],'>':[2,1]}

codes=[]
for line in f.readlines():
    codes.append(line.strip())

for i in codes:
    seq=mapkeypad(i)
    print(i,seq)


