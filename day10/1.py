f = open("input.txt")

#Need to think about approach here, gut feel is a directed graph (per start point?) as there could be multiple paths to the same end point, although I could handle this by adding end points to a set for each start point and summing them...

#Current plan: build 2d grid of values (list of lists), iterate through the grid, if it's a 0, start a recursive search for paths to 9 (add 9s to set to only count uniques), add set total to running total, repeat until we've checked the whole grid for 0s.

grid=[]
sdirs=[[0,-1],[1,0],[0,1],[-1,0]] #n,e,s,w

def find_paths(x,y,num,found):
#    print("finding ",num+1," next to ",x,y)
    for sdir in sdirs:
        #bounds check
        nx=x+sdir[0]
        if nx<0 or nx>xmax: continue
        ny=y+sdir[1]
        if ny<0 or ny>ymax: continue
        if grid[ny][nx]==num+1:
#            print("found a ",num+1," at: ",nx,ny)
            if num+1==9:
                found.add((str(nx)+"."+str(ny)))
            else:
                find_paths(nx,ny,num+1,found)
    return found
index=0
for line in f.readlines():
    grid.append([])
    for char in line.strip():
        grid[index].append(int(char))
    index+=1

xmax=len(grid[0])-1
ymax=len(grid)-1

paths=0
for y in range(len(grid)):
    for x in range(len(grid[y])):
#        print ("testing:", x,y,grid[y][x])
        if grid[y][x]==0:
            found=set()
            found=find_paths(x,y,grid[y][x],found)
            paths+=len(found)

#print(grid)
print(paths)
