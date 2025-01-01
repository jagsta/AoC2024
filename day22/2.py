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

for i in range(nsecrets):
    for i,secret in enumerate(secrets):
        secrets[i]=gen_secret(secret)
total=0
for secret in secrets:
    total+=secret
    print(secret)
print("total:",total)
