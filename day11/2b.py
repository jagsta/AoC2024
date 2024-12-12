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

#Rethink time, too complicated to wrap my head around :/



from timeit import default_timer as timer
import math

f = open("input.txt")

def process_number(n,target):
#    print("processing ",n," at blinks",target)
    count=0
    if (target==0):
#        print(n," bottomed out, adding 1 to count")
        return 1
    if (n+"."+str(target)) in cache:
        #we know this product already
#        print("cache hit for",n+"."+str(target))
#        hits+=1
        return cache[n+"."+str(target)]
#   No cache hit, so carry on
    if n=="0":
        count+=process_number("1",target-1)
    elif len(n) % 2==1:
        #odd
        count+=process_number(str(int(n)*2024),target-1)
    else:
        #even
        j=int(len(n)/2)
#        print ("found even number of digits",n)
        num1=int(n[:j])
        num2=int(n[j:])
        count+=process_number(str(num1),target-1)
        count+=process_number(str(num2),target-1)
#        print ("odd length: ",n)
    cache[n+"."+str(target)]=count
#    print("Adding ",n+"."+str(target),count," to cache")
    return count



stones=[]
for number in f.readline().split():
    stones.append(number.strip())
#    print (stones)

hits=0
cache={}
count=0
targetblinks=75
for blinks in range(targetblinks):
    for n in stones:
        blinks+=1
#        print("processing ",n, "at ",blinks,"blinks")
        result=process_number(str(n),blinks)
        if blinks==targetblinks:
            count+=result
#        print("finished ",n," with result",result,"total",count)
#    nx.draw_networkx(g,arrows=True)
#    plt.show()
#print(len(cache))
#print(cache)
print("Total stones after",targetblinks,"is",count,"with")
