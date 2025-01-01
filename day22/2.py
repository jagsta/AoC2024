import sys

file="input.txt"

def mix(secret,value):
    secret=secret^value
    return secret

def prune(secret):
    value=secret % 16777216
    return value

def gen_secret(secret):
    t=secret*64
    secret=mix(secret,t)
    secret=prune(secret)
    t=secret//32
    secret=mix(secret,t)
    secret=prune(secret)
    t=secret*2048
    secret=mix(secret,t)
    secret=prune(secret)
    return secret

if len(sys.argv)>1:
    file=sys.argv[1]

f = open(file)

secrets=[]
for line in f.readlines():
    secrets.append(int(line.strip()))

nsecrets=2000
freq={}

for i,secret in enumerate(secrets):
    diff1=0
    diff2=0
    diff3=0
    diff4=0
    last=secret
    for c in range(nsecrets):
        diff4=diff3
        diff3=diff2
        diff2=diff1
        s=gen_secret(last)
        secrets[i]=s
        diff1=int(str(s)[-1])-int(str(last)[-1])
        last=s
        if c>2:
            if str(diff1)+"."+str(diff2)+"."+str(diff3)+"."+str(diff4) in freq:
                if secret not in freq[str(diff1)+"."+str(diff2)+"."+str(diff3)+"."+str(diff4)]["secret"]:
                    freq[str(diff1)+"."+str(diff2)+"."+str(diff3)+"."+str(diff4)]["secret"].append(secret)
                    freq[str(diff1)+"."+str(diff2)+"."+str(diff3)+"."+str(diff4)]["total"]+=int(str(last)[-1])
                    freq[str(diff1)+"."+str(diff2)+"."+str(diff3)+"."+str(diff4)]["count"]+=1
            else:
                freq[str(diff1)+"."+str(diff2)+"."+str(diff3)+"."+str(diff4)]={}
                freq[str(diff1)+"."+str(diff2)+"."+str(diff3)+"."+str(diff4)]["secret"]=[secret]
                freq[str(diff1)+"."+str(diff2)+"."+str(diff3)+"."+str(diff4)]["total"]=int(str(last)[-1])
                freq[str(diff1)+"."+str(diff2)+"."+str(diff3)+"."+str(diff4)]["count"]=1


total=0
for secret in secrets:
    total+=secret
    print(secret)
print("total:",total)

mostfreq=0
mostval=0
mf=""
mv=""
for seq,value in freq.items():
    if value["count"]>mostfreq:
        mostfreq=value["count"]
        mf=seq+":"+str(value["count"])+":"+str(value["total"])
    if value["total"]>mostval:
        mostval=value["total"]
        mv=seq+":"+str(value["count"])+":"+str(value["total"])
    print(seq, "count",value["count"],"total", value["total"])
print("most frequent",mf)
print("most valuable",mv)
