import sys

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f = open(file)

keys=[]
locks=[]

inlock=False
l=0
ki=0
li=0
for line in f.readlines():
    if l==0:
        if line.strip()=="#####":
            print("In lock")
            inlock=True
            locks.append([0]*5)
        else:
            print("In key")
            inlock=False
            keys.append([0]*5)
        l+=1
    elif line.strip()=="":
        if inlock:
            li+=1
        else:
            ki+=1
        l=0
    else:
        if inlock:
            for i,c in enumerate(line.strip()):
                if c=="#":
                    locks[li][i]+=1
            l+=1
        else:
            if l<6:
                for i,c in enumerate(line.strip()):
                    if c=="#":
                        keys[ki][i]+=1
                l+=1
matches=0
for key in keys:
    for lock in locks:
        fits=1
        for i in range(5):
            if lock[i]+key[i]>5:
                fits=0
                break
        if fits:
            matches+=1


print(len(keys),keys)
print(len(locks),locks)
print("matches:",matches)
