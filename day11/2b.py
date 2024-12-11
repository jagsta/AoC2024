#This can't work by brute force for blinks = 75
# Odd length numbers > 99 need to be computed until the result is an even length
# Any even length number length 2^n will decompose into single digits in n blinks
# Any other even number will decompose to 2 odd length numbers, and will need computing
# Any single digit will decompose to a set of single digits in a fixed number of blinks - 0(1), 1,2,3,4(3), 5,6,7,8,9(5)
# precompute the trees for 0 - 9, these can replace any instances of a single digit
# We don't care about intermediates, we only care about the number of nodes at depth = blinks
# We can skip any calculations until we exceed the target blinks on a given tree, then back track to the right number of blinks
#
# For each starting stone, traverse the tree, skipping, until blinks>target
# We'll need to do this recursively, depth first?
# When we exceed the target, we'll add the number of nodes at the correct depth to a count of nodes, then carry on
# Iterate over the initial stones tallying up the nodes


from timeit import default_timer as timer
import math
import networkx as nx
import matplotlib.pyplot as plt

class memo:
    maxdepth=0
    depth={}

f = open("input.txt")

def process_number(n,adepth,rdepth,target):
    print("processing ",n," at depth",depth)
    if (adepth==target):
#        print(n," is at depth ",depth," adding 1 to count")
        return 1
    count=0
    if n in cache:
        #are we more than maxdepth?
        if rdepth>cache[n].maxdepth:
            cache[n].maxdepth=rdepth
            cache[n].depth[rdepth].append(n)
        #how many blinks can we skip?
        skip=cache[n].maxdepth
        if adepth+skip>target:
            #too much, see if we have the right number
            if cache[n].depth[target-adepth]:
                #process each number at that depth
                for i in cache[n].depth[target-adepth]:
                    count+=1
                return count
            else:
                # Nope, what's the best we can do?
                best=target-adepth
                while not cache[n].depth[i]:
                    best-=1
                for i in cache[n].depth[best]:
                    count+=process_number(i,adepth+best,rdepth+best,target)
        else:
            #we can jump maxdepth
            for i in cache[n].depth[maxdepth]:
                count+=process_number(i,adepth+cache[n].maxdepth,rdepth+cache[n].maxdepth,target)
    else:
        #new number, add to cache
        cache[n]=memo()
        rdepth=1
    if n=="0":
 #       g.add_edge(n,"1")
        count+=process_number("1",adepth+1,rdepth,target)
    elif len(n) % 2==1:
        #odd
 #       g.add_edge(n,str(int(n)*2024))
        count+=process_number(str(int(n)*2024),adepth+1,rdepth,target)
    else:
        #even
        j=int(len(n)/2)
#        print ("found even number of digits",n)
        num1=int(n[:j])
        num2=int(n[j:])
#        g.add_edge(n,str(num1))
        count+=process_number(str(num1),adepth+1,rdepth,target)
#        g.add_edge(n,str(num2))
        count+=process_number(str(num2),adepth+1,rdepth,target)
#        print ("odd length: ",n)

    return count



stones=[]
for number in f.readline().split():
    stones.append(number.strip())
#    print (stones)

cache={}
count=0
skips=0
depth=0
g=nx.DiGraph()
targetblinks=5
for n in stones:
    start=timer()
    print("processing ",n, "at depth",depth)
    result=process_number(str(n),depth,targetblinks)
    count+=result
    end=timer()
    print("finished ",n," with result",result,"in ",end-start,"total",count)
#    nx.draw_networkx(g,arrows=True)
#    plt.show()
print(count)
print(len(cache))
#print(cache)
print(g.number_of_edges())
