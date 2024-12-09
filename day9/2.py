f = open("input.txt")

#one big line of input, parse char by char, and add to an array - either as <id> or as space, based on the value of the char
#This gets me to a file layout, one block per array index
#Iterate from the beginning and end, moving blocks from end to spaces from beginning, until the two cross over

blocks=[]
space=0 #0=file,1=space
fid=0
for char in f.readline().strip():
    size = int(char)
    if not space:
        if size==0:
            space=1
        for i in range(size):
            blocks.append(fid)
            space=1
        fid+=1
    elif space:
        if size==0:
            space=0
        for i in range(size):
            blocks.append(None)
            space=0
#print(blocks)
#Compactify the filesystem
lindex=0
rindex=len(blocks)-1
while (rindex>lindex):
#    print (lindex,rindex)
    if blocks[lindex] is not  None:
        lindex+=1
        continue
    elif blocks[rindex] is not None:
        blocks[lindex]=blocks[rindex]
        blocks[rindex]=None
    rindex-=1

#Do the math
total=0
for i in range(len(blocks)):
    if blocks[i] is not None:
        total=total+(blocks[i]*i)
print ("Checksum: ",total)
