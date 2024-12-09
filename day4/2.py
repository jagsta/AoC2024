word=["M","A","S"]
directions=[[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
dir1=[[-1,-1],[1,1]]
dir2=[[1,-1],[-1,1]]
wordsearch=[]
max_x=0
max_y=0
wordindex=0
total=0
wordlen=len(word)
f = open("input.txt")
for line in f.readlines():
    wordsearch.append(line.rstrip())
max_y=len(wordsearch)
max_x=len(wordsearch[0])

print (max_x,max_y)
#print (wordsearch)

def find_letter (position, wordindex, seek_dir):
    seek=word[wordindex]
    cur_x=position[0]
    cur_y=position[1]
    new_x=cur_x+seek_dir[0]
    new_y=cur_y+seek_dir[1]
    if (new_x>=0 and new_y>=0 and new_x<max_x and new_y<max_y):
        if wordsearch[new_x][new_y]==seek:
            if wordindex<wordlen-1:
                found=find_letter([new_x,new_y],wordindex+1,seek_dir)
                return(found)
            else: return(1)
        else: return(0)
    else: return(0)

for x in range(max_x):
    for y in range(max_y):
        if wordsearch[x][y]=="A" and x>0 and y>0 and x<max_x-1 and y<max_y-1:
            if ((wordsearch[x-1][y-1]=="M" and wordsearch[x+1][y+1]=="S") or (wordsearch[x-1][y-1]=="S" and wordsearch[x+1][y+1]=="M")):
                if ((wordsearch[x+1][y-1]=="M" and wordsearch[x-1][y+1]=="S") or (wordsearch[x+1][y-1]=="S" and wordsearch[x-1][y+1]=="M")):
                    total+=1


print(total)
