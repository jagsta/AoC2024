f = open("input.txt")

#one big line of input, parse char by char, and add to an array - either as <id> or as space, based on the value of the char
#This gets me to a file layout, one block per array index
#Iterate from the beginning and end, moving blocks from end to spaces from beginning, until the two cross over

#Bleurgh, I don't think my data structure is great for part 2
#From end of array, find a file id, iterate till the end of that file to find size, repeat until fid=0
#Then iterate from beginning of array with a window of that size, looking for all Nones, if one is found, write the file id to those positions, and overwrite the files original positions with None
#Then do the math

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
print(blocks)
#Compactify the filesystem

rindex=len(blocks)-1
#print (len(blocks),rindex,fid, blocks[-1])
while (fid>0):
    fid-=1
    filesize=0
#    print (len(blocks),rindex,fid, blocks[rindex])
    while blocks[rindex] != fid:
#        print(fid,rindex)
        rindex-=1
    while(blocks[rindex]==fid):
        filesize+=1
        rindex-=1
#    print(rindex,fid,filesize)
    found=0
    lindex=0
    while(found==0 and (lindex+filesize)<len(blocks) and lindex+filesize-1<rindex+1):
        window=blocks[lindex:lindex+filesize]
#        print(window)
        if (window.count(None) == len(window)):
#            print("found a space!",lindex)
            #it fits!
            found=1
            for i in range(len(window)):
                blocks[lindex+i]=fid
                blocks[rindex+i+1]=None
#            print(blocks)
        else:
            lindex+=1

print(blocks)
#Do the math
total=0
for i in range(len(blocks)):
    if blocks[i] is not None:
        total=total+(blocks[i]*i)
print ("Checksum: ",total)
