f = open("input.txt")

#one big line of input, parse char by char, and add to an array - either as <id> or as space, based on the value of the char
#This gets me to a file layout, one block per array index
#Iterate from the beginning and end, moving blocks from end to spaces from beginning, until the two cross over

#Bleurgh, I don't think my data structure is great for part 2
#From end of array, find a file id, iterate till the end of that file to find size, repeat until fid=0
#Then iterate from beginning of array with a window of that size, looking for all Nones, if one is found, write the file id to those positions, and overwrite the files original positions with None
#Then do the math

#This runs like dog poo, maybe use lists of files and spaces to speed the ordering up and avoid the sliding window, which is clearly very slow
def defrag(fid):
    size=files[fid][0]
    end=files[fid][1]
#    print("fid:",fid," size:",size)
    # find the first gap which fits
    for i in range(len(gaps)):
        if gaps[i][0]==size and gaps[i][1]<files[fid][1]:
#           print("fits exactly in ",size)
            files[fid][1]=gaps[i][1]
            gaps.pop(i)
            break
        elif gaps[i][0]>size and gaps[i][1]<files[fid][1]:
#            print("gap too big by ",gaps[i][0]-size,"remainder index is ",gaps[i][1]+size)
            files[fid][1]=gaps[i][1]
            gaps[i][0]-=size
            gaps[i][1]+=size
            break

files=[]
gaps=[]
blocks=[]
index=0
space=0 #0=file,1=space
fid=0
for char in f.readline().strip():
    size = int(char)
    if not space:
        if size==0:
            space=1
        files.append([size,index])
        for i in range(size):
            blocks.append(fid)
            space=1
        fid+=1
    elif space:
        if size==0:
            space=0
        else:
            gaps.append([size,index])
        for i in range(size):
            blocks.append(None)
            space=0
    index+=size
#print(files)
#print(gaps)
#print(blocks)
#Compactify the filesystem
#try the new way
for file in reversed(range(len(files))):
    defrag(file)
#print(files)
#print(gaps)
newtotal=0
for i in range(len(files)):
    for j in range(files[i][0]):
        newtotal+=(i*(files[i][1]+j))
print(newtotal)

